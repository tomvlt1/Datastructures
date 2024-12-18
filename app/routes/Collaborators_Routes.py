# this file should define the collaborators blueprint which is meant to administer
# the displaying as well as filtering of collaborator data.
# this file englobes functionalities for displaying the full list of collaborators
# and moreover handling search queries for collaborators based on user input

from flask import Blueprint, render_template, request, jsonify
from Filter import filter_data, filter_data_fullname
from Display import AddSortValue
from userclass import User 

collaborators_bp = Blueprint('collaborators', __name__)

# the function below manages GET and POST requests to display and filter collaborators
# given specified filters
@collaborators_bp.route('/', methods=['GET', 'POST'])
def collaborators():
    try:
        if request.method == 'POST':  
            data_json =User.load_all_user_data() 
            # Get the filter values from the request
            filters_values = request.get_json() #get_json from the html form. Using json for it to go faster
            print("Received filters:", filters_values) #to see what the post of the user is.
            # Filter the data based on the filters
            filtered_data = filter_data(filters_values, data_json)  
            
            looking_for = ''
            looking_for_degree =''     
            for key, value in filters_values.items(): #items helps you iterate throuth the dictionary, it returns the key: Value
                if value !='':
                    if key == 'looking_for':
                        looking_for = value  
                               
                    elif key == 'looking_for_degree':
                        looking_for_degree = value
                      
            sorted_data = AddSortValue(filtered_data, looking_for, looking_for_degree)   
            # Convert sorted data to dictionary (json). todict
            data_json = sorted_data.to_dict(orient='records')             
            vtot=len(data_json)
            
            return jsonify({'data':data_json,'vtot': vtot})

        else:
            # If no POST data is sent, return the full data
            data_json =User.load_all_user_data()  
            vtot=len(data_json)
            
            return render_template('collaborators.html', data=data_json,vbinary='',vtot=vtot)        
           

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

# the function below is meant to handle the seach functionality for collaborators
# also filtering and displaying collaborators based on search query
@collaborators_bp.route('/search_collaborators', methods=[ 'POST'])
def search_collaborators():
    try:
        if request.method == 'POST':  
           
            data_json =User.load_all_user_data() 
            # Get the filter values from the request
            search_query=request.form.get('search_query').strip()
           
            if search_query==None or search_query=='':
                pass
 
            # Filter the data based on the filters
            vbinary=User.full_names(search_query)
          
            filtered_data = filter_data_fullname(search_query, data_json)  
            sorted_data = AddSortValue(filtered_data,'', '')  
           
            # Convert sorted data to dictionary (json). todict
            data_json = sorted_data.to_dict(orient='records')  
            total_recs=len(data_json)           
            vtot=len(data_json)
            return render_template('collaborators.html', data=data_json,vbinary=vbinary,vtot=vtot)


    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

