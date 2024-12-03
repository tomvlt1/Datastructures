from flask import Blueprint, render_template, request, jsonify
from Filter import filter_data,filter_data_fullname
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
            vtot=len(data_json)
            
            return jsonify({'data':data_json,'vtot': vtot})

        else:
            # If no POST data is sent, return the full data
            data_json =User.load_mentor_user_data()     
            vtot=len(data_json)
            
            return render_template('mentors.html', data=data_json,vbinary='',vtot=vtot)
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
@mentors_bp.route('/search_mentors', methods=[ 'POST'])
def search_mentors():
    try:
        if request.method == 'POST':           
            data_json =User.load_mentor_user_data()
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
            vtot=len(data_json)
            return render_template('mentors.html', data=data_json,vbinary=vbinary,vtot=vtot)

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500