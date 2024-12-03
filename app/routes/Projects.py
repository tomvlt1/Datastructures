from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from projectclass import Project
from datetime import datetime
from validation import  validate_project_data
from Filter_projects import filter_projects,filter_data_fullname
from Display import AddSortValueProjects
import csv


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
            vtot=len(data_json)            
            return jsonify({'data':data_json,'vtot': vtot})
        else:
            # If no POST data is sent, return the full data
            data_json =Project.load_all_projects_data()   
            vtot=len(data_json)
            return render_template('projects.html', data=data_json,vbinary='',vtot=vtot)       
           

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
@projects_bp.route('/Myprojects', methods=['GET', 'POST'])   
def Myprojects():
    if session.get('IsLogged') != True:
      
       return render_template('login.html')
    
    try:
        if request.method == 'POST':  
            data_json =Project.load_all_projects_data(session['email'])
            # Get the filter values from the request
            filters_values = request.get_json() #get_json from the html form. 
            print("Received filters:", filters_values) 
            # Filter the data based on the filters
            filtered_data = filter_projects(filters_values, data_json)  
            
            looking_for = ''
            looking_for_positions_needed =''     
            for key, value in filters_values.items(): 
                if value !='':
                    if key == 'looking_for':
                        looking_for = value  
                               
                    elif key == 'looking_for_positions_needed':
                        looking_for_positions_needed = value
                      
            sorted_data = AddSortValueProjects(filtered_data, looking_for, looking_for_positions_needed)   
            # Convert sorted data to dictionary (json). todict
            data_json = sorted_data.to_dict(orient='records')  
            vtot=len(data_json)           
            return jsonify({'data':data_json,'vtot': vtot})

        else:
            # If no POST data is sent, return the full data
            data_json =Project.load_all_projects_data(session['email'])      
          
            vtot=len(data_json)
            return render_template('Myprojects.html', data=data_json,vbinary='',vtot=vtot)
      

    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500
    
@projects_bp.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if session.get('IsLogged') != True:
        session['createdP'] = 1
        return render_template('login.html')
    
    if request.method == 'POST':
    
        project_name = request.form.get('project_name')
        admin = session['email'] 
        number_of_people = request.form.get('number_of_people')
        keywords = request.form.get('keywords')  
        project_stage = request.form.get('project_stage')
        language_spoken = request.form.get('language_spoken')
        start_date = request.form.get('start_date')  
        completion_estimate = request.form.get('completion_estimate')  
        project_description = request.form.get('project_description')
        positions_needed = request.form.get('positions_needed')  
       # Process keywords and positions_needed into lists
            # Para keywords
        keywords_str = f"['{', '.join([keyword.strip() for keyword in keywords.split(',')])}']" if keywords else "[]"
        keywords_list= keywords_str
        # Para positions_needed
        positions_needed_str = f"['{', '.join([position.strip() for position in positions_needed.split(',')])}']" if positions_needed else "[]"
        positions_needed_list=positions_needed_str

        id_project=get_max_id_project()+1
        # Create Project object
        project = Project(
            project_name=project_name,
            admin=admin,
            number_of_people=number_of_people,
            keywords=keywords_list,
            project_stage=project_stage,
            language_spoken=language_spoken,
            start_date=start_date,
            completion_estimate_months=completion_estimate,
            project_description=project_description,
            positions_needed=positions_needed_list,
            sort_value=0,
            id_project=id_project
        )
        
      
         # Validate user data
        is_valid,verr= validate_project_data(project,0)
       
        if not is_valid:
            return render_template('createProject.html', admin=session['email'],error_message=verr)

        # Save new project to CSV (you can adapt this to use a database)
        try:
           
            Project.save_to_csv(project)
        except Exception as e:
            return render_template('createProject.html', error_message=f"Error saving project: {e}")

        # Redirect to project listing or detail page after successful creation
        data_json =Project.load_all_projects_data(session['email'])       
        return render_template('Myprojects.html', data=data_json)


    else:
        return render_template('createProject.html',admin=session['email'])

@projects_bp.route('/project/consult', methods=['POST'])
def projectconsult():
    project_id = request.form.get('id_project')  # Obtener el ID del proyecto desde el formulario

    if not project_id:
        print("Project not found.")

    try:
        # Intentamos obtener los datos del proyecto usando el ID
        project_id = int(project_id)  # Aseguramos que el ID es un número
        project_data = Project.get_project_data_from_csv(project_id)  # Buscar los datos del proyecto

        if not project_data:
            # Si no se encuentran los datos, podemos mostrar un mensaje o redirigir
            print("Project not found.")

        # Si el proyecto se encuentra, renderizamos los datos
        return render_template('Project.html', project_data=project_data)

    except ValueError:
        # Si ocurre un error al intentar convertir el ID en entero
        print("Invalid Project ID format.")

    except Exception as e:
        # Cualquier otra excepción que pueda ocurrir
        print(e)

@projects_bp.route('/project/view', methods=['POST'])
def viewproject():
    project_id = request.form.get('id_project')  # Obtener el ID del proyecto desde el formulario

    if not project_id:
        print("Project not found.")

    try:
        # Intentamos obtener los datos del proyecto usando el ID
        project_id = int(project_id)  # Aseguramos que el ID es un número
        project_data = Project.get_project_data_from_csv(project_id)  # Buscar los datos del proyecto

        if not project_data:
            # Si no se encuentran los datos, podemos mostrar un mensaje o redirigir
            print("Project not found.")

        # Si el proyecto se encuentra, renderizamos los datos
        return render_template('viewproject.html', project_data=project_data)

    except ValueError:
        # Si ocurre un error al intentar convertir el ID en entero
        print("Invalid Project ID format.")

    except Exception as e:
        # Cualquier otra excepción que pueda ocurrir
        print(e)

        
@projects_bp.route('/update_project', methods=['GET', 'POST'])
def update_project():   
    if request.method == 'POST':
        id_project = request.form.get('id_project')
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
       # Process keywords and positions_needed into lists
            # Para keywords
        keywords_str = f"['{', '.join([keyword.strip() for keyword in keywords.split(',')])}']" if keywords else "[]"
        keywords_list= keywords_str
        # Para positions_needed
        positions_needed_str = f"['{', '.join([position.strip() for position in positions_needed.split(',')])}']" if positions_needed else "[]"
        positions_needed_list=positions_needed_str


        # Create Project object
        project = Project(
            project_name=project_name,
            admin=admin,
            number_of_people=number_of_people,
            keywords=keywords_list,
            project_stage=project_stage,
            language_spoken=language_spoken,
            start_date=start_date,
            completion_estimate_months=completion_estimate,
            project_description=project_description,
            positions_needed=positions_needed_list,
            sort_value=0.0,
            id_project=id_project
        )
        
      
         # Validate user data
        is_valid,verr= validate_project_data(project,1)
       
        if not is_valid:
           return render_template('Project.html', project_data=project,error_message=verr)

        # Save new project to CSV (you can adapt this to use a database)
        try:
           
            Project.save_to_csv(project)
        except Exception as e:
       
            return render_template('Project.html', project_data=project,error_message=f"Error saving project: {e}")

        # Redirect to project listing 
        data_json =Project.load_all_projects_data(admin)       
        return render_template('Myprojects.html', data=data_json)
   
def get_max_id_project():
    max_id = 0  # Inicializamos con 0, asumiendo que los IDs son números enteros
    try:
        with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Verificar si el campo 'id_project' está presente y es un número
                try:
                    current_id = int(row['id_project'])  # Convertimos el id a un número
                    if current_id > max_id:
                         max_id = current_id  # Actualizamos el max_id si encontramos uno mayor
                except ValueError:
                    continue  # Si no se puede convertir el valor a entero, se ignora
    except FileNotFoundError:
        pass
    return max_id

@projects_bp.route('/search_projects', methods=[ 'POST'])
def search_projects():
    try:
        if request.method == 'POST':  
           
            data_json =Project.load_all_projects_data()
            # Get the filter values from the request
            search_query=request.form.get('search_query').strip()
           
            if search_query==None or search_query=='':
                pass
 
            # Filter the data based on the filters
            vbinary=Project.full_names(search_query)
          
            filtered_data = filter_data_fullname(search_query, data_json)  
            sorted_data =  AddSortValueProjects(filtered_data,'', '')  
           
            # Convert sorted data to dictionary (json). todict
            data_json = sorted_data.to_dict(orient='records')          
            vtot=len(data_json)
            return render_template('projects.html', data=data_json,vbinary=vbinary,vtot=vtot)


    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500

@projects_bp.route('/search_myprojects', methods=[ 'POST'])
def search_myprojects():
    try:
        if request.method == 'POST':  
           
            data_json =Project.load_all_projects_data(session['email'])
            # Get the filter values from the request
            search_query=request.form.get('search_query').strip()
           
            if search_query==None or search_query=='':
                pass
 
            # Filter the data based on the filters
            vbinary=Project.full_names(search_query)
          
            filtered_data = filter_data_fullname(search_query, data_json)  
            sorted_data =  AddSortValueProjects(filtered_data,'', '')  
           
            # Convert sorted data to dictionary (json). todict
            data_json = sorted_data.to_dict(orient='records')  
                 
            vtot=len(data_json)
            return render_template('Myprojects.html', data=data_json,vbinary=vbinary,vtot=vtot)


    except Exception as e:
        print(f"An error occurred: {e}")
        
        # Return an error response if something goes wrong
        return jsonify({'error': 'An unexpected error occurred'}), 500