from flask import Blueprint, render_template, request, jsonify
from Filter import filter_data
from Display import AddSortValue
from userclass import User 

mentors_bp = Blueprint('mentors', __name__)

@mentors_bp.route('/', methods=['GET', 'POST']) 

def mentors():
    try:
        if request.method == 'POST':  
            data_json =User.load_mentor_user_data()
            # Get the filter values from the request
            filters_values = request.get_json()
            print("Received filters:", filters_values) 
            # Filter the data based on the filters
            filtered_data = filter_data(filters_values, data_json)  
        
            looking_for = ''
            looking_for_degree =''     
            for key, value in filters_values.items():
                if value!='':
                    if key == 'looking_for':
                        looking_for =value                 
                    elif key == 'looking_for_degree':
                        looking_for_degree = value
            
            sorted_data = AddSortValue(filtered_data, looking_for, looking_for_degree)        
            # Convert sorted data to dictionary
            data_json = sorted_data.to_dict(orient='records')          

            return jsonify({'data':  data_json})

        else:
            # If no POST data is sent, return the full data
            data_json =User.load_mentor_user_data()     
            
            return render_template('mentors.html', data=data_json)

    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

