# Overall Comment:
# This code defines a Flask Blueprint called 'mentors' to handle routes related to mentors page.

from flask import Blueprint, render_template, request, jsonify
from Filter import filter_data, filter_data_fullname
from Display import AddSortValue
from userclass import User 

mentors_bp = Blueprint('mentors', __name__)

@mentors_bp.route('/', methods=['GET', 'POST']) 
def mentors():
    # This route handles both GET and POST requests.
    # GET: It will render all mentor data in a template, without any input of the user.
    # POST: Applies the inputetd filters and returns filtered data with its sort value.
    # It uses methods from the class user in order to handle the data.
    # It also uses funtions to filter the data that are inported from 'Filter' file.
    # Finally, it adds the sort value and sorts it by it using a function imported from the 'Display' file.
    try:
        if request.method == 'POST':  
            # When receiving a POST request, get the mentor data
            data_json = User.load_mentor_user_data()
            
            # Get the filter values from the request as JSON
            filters_values = request.get_json()
            print("Received filters:", filters_values) 
            
            filtered_data = filter_data(filters_values, data_json)  
        
            looking_for = ''
            looking_for_degree =''     
            for key, value in filters_values.items():
                if value!='':
                    if key == 'looking_for':
                        looking_for = value                 
                    elif key == 'looking_for_degree':
                        looking_for_degree = value
            
            # Sort the filtered data using the AddSortValue function
            sorted_data = AddSortValue(filtered_data, looking_for, looking_for_degree)     
            
            # Convert the sorted DataFrame to a list of dictionaries 
            data_json = sorted_data.to_dict(orient='records')          
            vtot = len(data_json)
            
            return jsonify({'data': data_json, 'vtot': vtot})

        else:
            # If no POST request is made, just show all mentors
            data_json = User.load_mentor_user_data()     
            vtot = len(data_json)
            
            # Render the mentors.html template with the full mentor data
            return render_template('mentors.html', data=data_json, vbinary='', vtot=vtot)
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

@mentors_bp.route('/search_mentors', methods=['POST'])
def search_mentors():
    # This route handles searching for mentors by a given name.
    # It only handles POST requests as we will only use it when the user searches for an specific name.
    # It uses a method from the user class to binary search for the given name and then filters the data.
    try:
        if request.method == 'POST':
            # Load mentor data
            data_json = User.load_mentor_user_data()

            # Get the search query from the POST form data
            search_query = request.form.get('search_query').strip()
            if search_query is None or search_query == '':
                pass  # If no search query, do not apply additional filtering
                
            # Perform a binary search for the search_query in full names
            vbinary = User.full_names(search_query)
            filtered_data = filter_data_fullname(search_query, data_json)
            sorted_data = AddSortValue(filtered_data, '', '')  
           
            # Convert sorted data to a list of dictionaries
            data_json = sorted_data.to_dict(orient='records')             
            vtot = len(data_json)
            
            return render_template('mentors.html', data=data_json, vbinary=vbinary, vtot=vtot)

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrng
        return jsonify({'error': 'An unexpected error occurred'}), 500
