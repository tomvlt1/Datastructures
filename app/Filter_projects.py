import datetime

def filter_projects(filters, data):
    filtered_data = []
    
    for project in data:
        match = True
        
        for key, filter_value in filters.items():
            if filter_value == '':
                continue
            
            if key == 'min_number_of_people':
                if float(project.get('Number of People', 0)) < float(filter_value):
                    match = False
                    break
            
            if key == 'max_number_of_people':
                if float(project.get('Number of People', 0)) > float(filter_value):
                    match = False
                    break
            
            if key == 'min_completion_estimate_months':
                if float(project.get('Completion Estimate (Months)', 0)) < float(filter_value):
                    match = False
                    break
            
            if key == 'max_completion_estimate_months':
                if float(project.get('Completion Estimate (Months)', 0)) > float(filter_value):
                    match = False
                    break
            
            if key == 'project_stage':
                if filter_value.lower() != project.get('Project Stage', '').lower():
                    match = False
                    break
            
            if key == 'language_spoken':
                if filter_value.lower() not in project.get('Language Spoken', '').lower():
                    match = False
                    break
            
            if key == 'start_date_from':
                try:
                    project_start_date = datetime.datetime.strptime(project.get('Start Date', ''), "%Y-%m-%d").date()
                    filter_start_date = datetime.datetime.strptime(filter_value, "%Y-%m-%d").date()
                    if project_start_date < filter_start_date:
                        match = False
                        break
                except ValueError:
                    match = False
                    break
            
            if key == 'start_date_to':
                try:
                    project_start_date = datetime.datetime.strptime(project.get('Start Date', ''), "%Y-%m-%d").date()
                    filter_end_date = datetime.datetime.strptime(filter_value, "%Y-%m-%d").date()
                    if project_start_date > filter_end_date:
                        match = False
                        break
                except ValueError:
                    match = False
                    break
        
        if match:
            filtered_data.append(project)
    
    return filtered_data

def filter_data_fullname(fullname, data):
    filtered_data = []
    #we are looping through each user in the data list
    for project in data:
        match = True  
        UserFullName=project.get('Project Name', '') 
        UserFullName= UserFullName.replace(" ", "")
        UserFullName=UserFullName.lower()
       
        fullname= fullname.replace(" ", "")
        fullname=fullname.lower() 
       
        # If the filter value is an empty string, we don't need to apply it
        if fullname == UserFullName :       
            filtered_data.append(project)
    # Return the filtered data
    return filtered_data