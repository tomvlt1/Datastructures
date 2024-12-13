#this file is responsible to manage project-related functinalities
#it includes routes for creating, updating, viewing, filtering as well as searching for projects.
#this file also manages validation, sessino-based access control and finally storage and retrieving 
#of project data from a csv

from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from projectclass import Project
from datetime import datetime
from validation import  validate_project_data
from Filter_projects import filter_projects,filter_data_fullname
from Display import AddSortValueProjects
import csv

projects_bp = Blueprint('projects', __name__)

# the function below should be able to administer the main projects page, process filter values,
# and finally return filter or sorted projects 
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

# the function below should be able to manage the user's personal project's page, 
# as well as process filters and lastly display filtered or sorted data 
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

# the function below has the objective to develop the functionality of creating a new projects
# along with validating the given input and finally saveing the project
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
            # to keywords
        keywords_str = f"['{', '.join([keyword.strip() for keyword in keywords.split(',')])}']" if keywords else "[]"
        keywords_list= keywords_str
        # to positions_needed
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

# the fucntion below should fetch and display details of a given project based on the project's id
@projects_bp.route('/project/consult', methods=['POST'])
def projectconsult():
    project_id = request.form.get('id_project')  
    if not project_id:
        print("Project not found.")

    try:
        project_id = int(project_id)  
        project_data = Project.get_project_data_from_csv(project_id)  

        if not project_data:
            print("Project not found.")

        return render_template('Project.html', project_data=project_data)

    except ValueError:
        print("Invalid Project ID format.")

    except Exception as e:
        print(e)

# the function below should render the details of a given project for viewing without modification
@projects_bp.route('/project/view', methods=['POST'])
def viewproject():
    project_id = request.form.get('id_project') 
    if not project_id:
        print("Project not found.")

    try:
        #trying to get the data of the project using the 
        project_id = int(project_id)  #ensure that the id is an integer
        project_data = Project.get_project_data_from_csv(project_id)  #search for the projects data

        if not project_data:
            #if the data is not found a message is printed
            print("Project not found.")

        #if the project is found the data is renderized 
        return render_template('viewproject.html', project_data=project_data)

    except ValueError:
        #in the case an error occurs when trying to convert the id into an integer
        print("Invalid Project ID format.")

    except Exception as e:
        #any other expression that may occur
        print(e)

# the function below has the goal to update an existing project after validating the input
# it finally saves the changes
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
            # for keywords
        keywords_str = f"['{', '.join([keyword.strip() for keyword in keywords.split(',')])}']" if keywords else "[]"
        keywords_list= keywords_str
        # for positions_needed
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

# the function below should retrieve the highest project id to ensure unique ids for new projects
def get_max_id_project():
    max_id = 0  #initialize with a zero assuming the ids are integers
    try:
        with open("generated_project_database.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # verify if the field 'id_project' is present and is a number
                try:
                    current_id = int(row['id_project'])  #converts the id into a number 
                    if current_id > max_id:
                         max_id = current_id  #update the max_id if a higher one is found
                except ValueError:
                    continue  #if it not possible to convert the entire value, ignore it
    except FileNotFoundError:
        pass
    return max_id

# the function below should allow users to search for projects using a query
# also applying filters and sorting before displaying results 
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

# the function below should enable logged-in users to search their own projects using a query
# with filters and sorting applied
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
