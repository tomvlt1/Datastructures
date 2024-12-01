from flask import Blueprint, render_template, request, jsonify
from Filter import filter_data, filter_data_fullname
from Display import AddSortValue
from userclass import User 

collaborators_bp = Blueprint('collaborators', __name__)

@collaborators_bp.route('/', methods=['GET', 'POST'])
def collaborators():
    try:
        if request.method == 'POST':  
            data_json =User.load_all_user_data() 
            # Get the filter values from the request
            filters_values = request.get_json() #get_json from the html form. 
            print("Received filters:", filters_values) 
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
           
            return jsonify({'data':  data_json})

        else:
            # If no POST data is sent, return the full data
            data_json =User.load_all_user_data()          
            return render_template('collaborators.html', data=data_json)

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
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
           
            return render_template('collaborators.html', data=data_json,vbinary=vbinary)

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

