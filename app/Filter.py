def filter_data(filters, data):
    filtered_data = []
    # Loop through each user in the data list
    for user in data:
        match = True  
        # Loop through the filters dictionary to check each filter
        for i, filter_value in filters.items():
            # If the filter value is an empty string, we don't need to apply it
            if filter_value == '':
                continue  # Skip this filter if it's empty
            if i == 'min_age':
                if float(user.get('Age', 0)) < float(filter_value):
                    match = False  
                    break
            if i == 'max_age':
                if float(user.get('Age', 0)) > float(filter_value):
                    match = False  
                    break
            if i == 'min_gpa':
                if float(user.get('GPA', 0)) < float(filter_value):
                    match = False  
                    break
            if i == 'max_gpa':
                if float(user.get('GPA', 0)) > float(filter_value):
                    match = False  
                    break
            if i == 'min_hours':
                if float(user.get('Availability', 0)) < float(filter_value):
                    match = False  
                    break
            if i == 'max_hours':
                if float(user.get('Availability', 0)) > float(filter_value):
                    match = False  
                    break
            if i == 'nationality':
                if filter_value.lower() != user.get('Nationality', '').lower():
                    match = False  
                    break
            if i == 'country_of_residence':
                if filter_value.lower() != user.get('Country of Residence', '').lower():
                    match = False  
                    break
            if i == 'degree':
                if filter_value.lower() not in user.get('Degree', '').lower():
                    match = False  
                    break
            if i == 'graduation_year':
                if filter_value != user.get('Graduation Year', ''):
                    match = False  
                    break           
        # If the user passed all the filters, add them to the filtered data list
        if match:
            filtered_data.append(user)
    # Return the filtered data
    return filtered_data

def filter_data_fullname(fullname, data):
    filtered_data = []
    # Loop through each user in the data list
    for user in data:
        match = True  
        UserFullName=user.get('First Name', '') + user.get('Last Name', '')
        UserFullName= UserFullName.replace(" ", "")
        UserFullName=UserFullName.lower()
        UserFullName1=user.get('Last Name', '') + user.get('First Name', '')
        UserFullName1= UserFullName.replace(" ", "")
        UserFullName1=UserFullName1.lower()   
        
        fullname= fullname.replace(" ", "")
        fullname=fullname.lower() 
       
                   # If the filter value is an empty string, we don't need to apply it
        if fullname == UserFullName or fullname == UserFullName1:       
            filtered_data.append(user)
    # Return the filtered data
    return filtered_data