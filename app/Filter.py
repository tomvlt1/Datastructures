#This file is responsible for filterinf of the data. 

#This function takes as an input the data that is being used by the application and the filters that a user applys when condicting a search on the colaborators
#The function filters by seeing if a case is between certain parametes, iterating through every possible user and every possible parameter, if one parameter does not match the filter imposed by the data then it is not used
def filter_data(filters, data):
    filtered_data = []
    # Loop through each user in the data list
    for user in data:
        match = True  
        # Loop through the filters dictionary to check each filter
        for i, filter_value in filters.items():
            # If the filter value is an empty string, we don't need to apply it
            if filter_value == '':
                continue  # Skip if empty .
            if i == 'min_age':
                if float(user.get('Age', 0)) < float(filter_value):
                    match = False  
                    print("Hola1")
                    break
            if i == 'max_age':
                if float(user.get('Age', 0)) > float(filter_value):
                    match = False  
                    print("Hola2")
                    break
            if i == 'min_gpa':
                if float(user.get('GPA', 0)) < float(filter_value):
                    match = False  
                    print("Hola3")
                    break
            if i == 'max_gpa':
                if float(user.get('GPA', 0)) > float(filter_value):
                    match = False  
                    print("Hola4")
                    break
            if i == 'min_hours':
                if float(user.get('Availability', 0)) < float(filter_value):
                    match = False  
                    print("Hola5")
                    break
            if i == 'max_hours':
                if float(user.get('Availability', 0)) > float(filter_value):
                    match = False  
                    print("Hola6")
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
        #If user passed all the filters add them to the list with the filltered data
        if match:
            filtered_data.append(user)
    return filtered_data

#This function is used to get all the names of individuals in the same format
def filter_data_fullname(fullname, data):
    filtered_data = []
    # Loop through each user in the data list getting the names in the same format, then the function compares the names to the one bieng searched and it filters the data bsed on weather ot not the name of the data matches the one being searched for
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
    return filtered_data
