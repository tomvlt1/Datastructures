import pandas as pd

def FilterAge(data, min_age, max_age):
    if min_age is not None:
        data = data[data['Age'] >= min_age]
        data = data[data['Age'] >= min_age]
    if max_age is not None:
        data = data[data['Age'] <= max_age]
        data = data[data['Age'] <= max_age]
    return data

def FilterNationality(data, nationality):
    return data[data['Nationality'].str.lower() == nationality.lower()]

def FilterCountryOfResidence(data, country):
    return data[data['Country of Residence'].str.lower() == country.lower()]

def FilterDegree(data, field):
    return data[data['Degree'].str.lower() == field.lower()]

def FilterGPA(data, min_gpa, max_gpa):
    if min_gpa is not None:
        
        data = data[data['GPA'] >= min_gpa]
    if max_gpa is not None:
        data = data[data['GPA'] <= max_gpa]
        
    return data

def FilterAvailability(data, min_hours):
    return data[data['Availability'] >= min_hours]

def FilterGraduationYear(data, year):
    if year:
        return data[data['Graduation_year'] == year]
    return data
    
def main():
    filtered_data = pd.read_csv('generated_database.csv')
    filtered_data = FilterAge(filtered_data, 20, 25)
    filtered_data = FilterNationality(filtered_data, "germany")
    filtered_data = FilterCountryOfResidence(filtered_data, "germany")
    filtered_data = FilterGPA(filtered_data, 8.0, 10.0)
    filtered_data = FilterAvailability(filtered_data, 10)
    filtered_data = FilterGraduationYear(filtered_data, 2028)
    return(filtered_data)



