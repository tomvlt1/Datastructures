from flask import Blueprint, render_template, request, jsonify
from LoadData import data as initial_data
from Filter import Filtered_Data
from Display import AddSortValue


collaborators_bp = Blueprint('collaborators', __name__)

 
@collaborators_bp.route('/', methods=['GET', 'POST']) # method POST is when the user inputs something and get the first time the user enters

def collaborators():

    print("hola1") #for debuging purposes

    try:

        if request.method == 'POST':

            filters_values = request.get_json() #this gets the values from the form of the filter in a dictionary format converting everything to a string

            print("Received filters", filters_values)

            #Get the values from the form

            #Fix the format of the numerical values received in the json

            min_age = int(float(filters_values.get('min_age', 0)))  #first to float then to in and value when it cannot convert it

            max_age = int(float(filters_values.get('max_age', 100)))  

            min_gpa = float(filters_values.get('min_gpa', 0.0))

            max_gpa = float(filters_values.get('max_gpa', 10.0))

            min_hours = float(filters_values.get('min_hours', 0.0))

            max_hours = float(filters_values.get('max_hours', 40.0))

            #Now get the rest values

            graduation_year = filters_values.get('graduation_year','0')                          

            nationality = filters_values.get('nationality')

            country_of_residence = filters_values.get('country_of_residence')

            degree = filters_values.get('degree')

            #get the data for the word embeeding

            looking_for =  filters_values.get('looking_for')

            looking_for_degree = filters_values.get('looking_for_degree')

            #filter the data

            filtered_data = Filtered_Data(initial_data,min_age,max_age,min_gpa,max_gpa,min_hours,max_hours,nationality,country_of_residence,degree,graduation_year)

            #word embedding

            sorted_data = AddSortValue(filtered_data, looking_for, looking_for_degree)

            data_json = sorted_data.to_dict(orient='records')  #convert the data to json before sending

            return jsonify({'data': data_json})

            
        else:

             #if the user didnt input anything, change the whole data to json and return it

            data_json = initial_data.to_dict(orient='records')

            print(data_json[0]) 

            return render_template('collaborators.html', data=data_json)

    except Exception as e:

        print(f"Error en la ruta de colaboradores: {e}")

        return jsonify({'error': 'Ocurrió un error en el servidor'}), 500