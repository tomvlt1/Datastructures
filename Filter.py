import pandas as pd

# Load the CSV file
data = pd.read_csv("generated_database.csv", header=None, names=[
    "first_name", "last_name", "age", "nationality", "country_of_residence", 
    "degree", "graduation_year", "gpa", "availability", "looking_for", 
    "email", "description", "additional_information"
])

data['age'] = pd.to_numeric(data['age'], errors='coerce') 
data['gpa'] = pd.to_numeric(data['gpa'], errors='coerce')  
data['availability'] = pd.to_numeric(data['availability'], errors='coerce') 

# Filtering functions 
def FilterAge(data, min_age, max_age):
    if min_age is not None:
        data = data[data['age'] >= min_age]
    if max_age is not None:
        data = data[data['age'] <= max_age]
    return data

def FilterNationality(data, nationality):
    return data[data['nationality'].str.lower() == nationality.lower()]

def FilterCountryOfResidence(data, country):
    return data[data['country_of_residence'].str.lower() == country.lower()]

def FilterDegree(data, degree):
    return data[data['degree'].str.lower() == degree.lower()]

def FilterGraduationYear(data, year):
    return data[data['graduation_year'] == year]

def FilterGPA(data, min_gpa, max_gpa):
    if min_gpa is not None:
        data = data[data['gpa'] >= min_gpa]
    if max_gpa is not None:
        data = data[data['gpa'] <= max_gpa]
    return data

def FilterAvailability(data, min_hours):
    return data[data['availability'] >= min_hours]

def FilterLookingFor(data, looking_for):
    return data[data['looking_for'].str.lower() == looking_for.lower()]



