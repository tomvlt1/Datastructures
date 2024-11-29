from flask import Blueprint, render_template, request, jsonify
from Filter_projects import filter_projects
from Display import AddSortValueProjects
from projectclass import Project

projects_bp = Blueprint('collaborators', __name__)

@projects_bp.route('/', methods=['GET', 'POST'])
def collaborators():
    try:
        if request.method == 'POST':  
            data_json =Project.load_all_projects_data() 
            # Get the filter values from the request
            filters_values = request.get_json() #get_json from the html form. 
            print("Received filters:", filters_values) 
            # Filter the data based on the filters
            filtered_data = filter_projects(filters_values, data_json)  
            
            looking_for = ''
            looking_for_positions_needed =''     
            for key, value in filters_values.items(): #items helps you iterate throuth the dictionary, it returns the key: Value
                if value !='':
                    if key == 'looking_for':
                        looking_for = value  
                               
                    elif key == 'looking_for_positions_needed':
                        looking_for_positions_needed = value
                      
            sorted_data = AddSortValueProjects(filtered_data, looking_for, looking_for_positions_needed)   
            # Convert sorted data to dictionary (json). todict
            data_json = sorted_data.to_dict(orient='records')             
           
            return jsonify({'data':  data_json})

        else:
            # If no POST data is sent, return the full data
            data_json =Project.load_all_projects_data()          
            return render_template('projects.html', data=data_json)

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

