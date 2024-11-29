from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from projectclass import Project
from datetime import datetime
from validation import  validate_project_data
from Filter_projects import filter_projects
from Display import AddSortValueProjects


projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/', methods=['GET', 'POST'])
def projects():
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
    

@projects_bp.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
    
        project_name = request.form.get('project_name')
        admin = request.form.get('admin')  
        number_of_people = request.form.get('number_of_people')
        keywords = request.form.get('keywords')  
        project_stage = request.form.get('project_stage')
        language_spoken = request.form.get('language_spoken')
        start_date = request.form.get('start_date')  
        completion_estimate = request.form.get('completion_estimate')  
        project_description = request.form.get('project_description')
        positions_needed = request.form.get('positions_needed')  

        try:
            number_of_people = int(number_of_people)
        except (ValueError, TypeError):
            return render_template('createProject.html', error_message="Invalid number of people.")

        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        except (ValueError, TypeError):
            return render_template('createProject.html', error_message="Invalid start date format. Use YYYY-MM-DD.")

        try:
            completion_estimate = int(completion_estimate)
        except (ValueError, TypeError):
            return render_template('createProject.html', error_message="Invalid completion estimate. Enter number of months.")

        # Process keywords and positions_needed into lists
        keywords_list = [keyword.strip() for keyword in keywords.split(',')] if keywords else []
        positions_needed_list = [position.strip() for position in positions_needed.split(',')] if positions_needed else []

        # Create Project object
        project = Project(
            project_name=project_name,
            admin=admin,
            number_of_people=number_of_people,
            keywords=keywords_list,
            project_stage=project_stage,
            language_spoken=language_spoken,
            start_date=start_date_obj,
            completion_estimate=completion_estimate,
            project_description=project_description,
            positions_needed=positions_needed_list
        )

        # Validate project data
        is_valid, error = validate_project_data(project)
        if not is_valid:
            return render_template('createProject.html', error_message=error)

        # Save new project to CSV (you can adapt this to use a database)
        try:
            Project.save_to_csv(project)
        except Exception as e:
            return render_template('createProject.html', error_message=f"Error saving project: {e}")

        # Redirect to project listing or detail page after successful creation
        return redirect(url_for('project.list_projects'))  # Adjust the endpoint as needed

    else:
        return render_template('createProject.html')
