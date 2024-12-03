from datetime import datetime

def validation_function(user,vorigen):
        vValid=0
        verr='' 
        if vorigen==0:  
            if not user.validate_email():
                error_message = "Invalid email format"
                vValid=1
                verr = verr + '<br>' + error_message
            if not user.validate_password():
                error_message = "Password must be at least 8 characters long, with at least one uppercase letter, one number, and one special character"
                vValid=1
                verr = verr + '<br>' + error_message          
            if user.email_exists(user.email):
                error_message = "Email is already registered"
                vValid=1
                verr = verr + '<br>' + error_message
     
        if not user.validate_age():
            error_message = "Age must be between 18 and 120"
            vValid=1
            verr = verr + '<br>' + error_message                 
        if not user.validate_dob():
            error_message = "Invalid date format for Date of Birth. Use YYYY-MM-DD"
            vValid=1
            verr = verr + '<br>' + error_message                
        if not user.validate_linkedin():
            error_message = "Invalid LinkedIn URL format"
            vValid=1
            verr = verr + '<br>' + error_message
        if not user.validate_GPA():
            error_message = "Incorrect format of the GPA field, try this format 6.8"
            vValid=1
            verr = verr + '<br>' + error_message
       
        return vValid, verr
    
    
def validate_project_data(project,vorigen):
    vValid = 0
    verr = ''
    #solo se verifica si existe el admin cuando se crea. No en update
    if vorigen==0:
        if not project.admin or project.admin.strip() == '':
                error_message = "Admin is required."
                vValid = 1
                verr += '<br>' + error_message
        else:        #  Check if the admin exists in the databas                    
            if project.admin_exists:
                error_message = "Admin does not exist."
                vValid=1
                verr = verr + '<br>' + error_message  
    
    if not project.project_name or project.project_name.strip() == '':
        error_message = "Project name is required."
        vValid = 1
        verr += '<br>' + error_message

    if not isinstance(project.number_of_people, int) or project.number_of_people <= 0:
        error_message = "Number of people must be a positive integer."
        vValid = 1
        verr += '<br>' + error_message

    allowed_stages = ['Idea', 'Planning', 'Execution', 'Completed']
    if project.project_stage not in allowed_stages:
        error_message = f"Project stage must be one of the following: {', '.join(allowed_stages)}."
        vValid = 1
        verr += '<br>' + error_message

    allowed_languages = ['English', 'Spanish', 'French', 'German']  # Extend this list as needed
    if project.language_spoken not in allowed_languages:
        error_message = f"Language spoken must be one of the following: {', '.join(allowed_languages)}."
        vValid = 1
        verr += '<br>' + error_message

    if not isinstance(project.start_date, str):
        error_message = "Invalid start date format. It must be a string in YYYY-MM-DD format."
        vValid = 1
        verr += '<br>' + error_message   
    try:
        # Intento convertir el string a un objeto datetime
        datetime.strptime(project.start_date, "%Y-%m-%d")
    except ValueError:
            error_message = "Invalid start date format. Use YYYY-MM-DD."
            vValid = 1
            verr += '<br>' + error_message

    if not isinstance(project.completion_estimate_months, int) or project.completion_estimate_months <= 0:
        error_message = "Completion estimate must be a positive integer representing months."
        vValid = 1
        verr += '<br>' + error_message


    if not project.project_description or project.project_description.strip() == '':
        error_message = "Project description is required."
        vValid = 1
        verr += '<br>' + error_message

    if project.positions_needed:
        if not isinstance(project.positions_needed, list) or not all(isinstance(pos, str) for pos in project.positions_needed):
            error_message = "Positions needed must be a list of position names."
            vValid = 1
            verr += '<br>' + error_message
        elif len(project.positions_needed) == 0:
            error_message = "At least one position is needed."
            vValid = 1
            verr += '<br>' + error_message


    if project.keywords:
        if not isinstance(project.keywords, list) or not all(isinstance(keyword, str) for keyword in project.keywords):
            error_message = "Keywords must be a list of keywords."
            vValid = 1
            verr += '<br>' + error_message
            
        
    return vValid, verr

