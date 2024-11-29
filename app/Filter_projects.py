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
