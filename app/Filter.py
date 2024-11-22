import pandas as pd

def FilterAge(data, min_age, max_age):

    #Fix the format of the numerical values

    data['Age'] = pd.to_numeric(data['Age'], errors='coerce').fillna(0).astype(int)

    if min_age is not None:

        data = data[data['Age'] >= min_age] 

    if max_age is not None:

        data = data[data['Age'] <= max_age] 
    return data
 
def FilterNationality(data, nationality):
    if nationality:

        return data[data['Nationality'].str.lower() == nationality.lower()]

    return data  


def FilterCountryOfResidence(data, country):
    if country:

        return data[data['Country of Residence'].str.lower() == country.lower()]

    return data 

 

def FilterDegree(data, field):
    if field:

        return data[data['Degree'].str.lower() == field.lower()]

    return data 

 

def FilterGPA(data, min_gpa, max_gpa):

    data['GPA'] = data['GPA'].replace('', 0)

    data['GPA'] = pd.to_numeric(data['GPA'], errors='coerce').fillna(0).astype(float) 

    if min_gpa is not None:

        data = data[data['GPA'] >= min_gpa] 

    if max_gpa is not None:

        data = data[data['GPA'] <= max_gpa]  

    return data


def FilterAvailability(data, min_hours=None, max_hours=None):

    data['Availability'] = pd.to_numeric(data['Availability'], errors='coerce').fillna(0).astype(int)

    if min_hours is not None and max_hours is not None:

        data = data[(data['Availability'] >= min_hours) & (data['Availability'] <= max_hours)]

    elif min_hours is not None:

        data = data[data['Availability'] >= min_hours]

    elif max_hours is not None:

        data = data[data['Availability'] <= max_hours]

    return data

 
def FilterGraduationYear(data, graduation_year=''):
    return data[data['Graduation Year'] == graduation_year]




def Filtered_Data(data,min_age,max_age,min_gpa,max_gpa,min_hours,max_hours,nationality,country_of_residence,degree,graduation_year):

        filtered_data = data

        filtered_data = FilterAge(filtered_data, min_age, max_age)

        filtered_data = FilterGPA(filtered_data, min_gpa, max_gpa)

        filtered_data = FilterAvailability(filtered_data, min_hours, max_hours)

        if nationality!="":

            filtered_data = FilterNationality(filtered_data, nationality)

        if country_of_residence!="":

            filtered_data = FilterCountryOfResidence(filtered_data, country_of_residence)

        if degree!="":

            filtered_data = FilterDegree(filtered_data, degree)

        if graduation_year !='0' :

            filtered_data = FilterGraduationYear(filtered_data, graduation_year)

        return filtered_data

   
def main():

    filtered_data = pd.read_csv('generated_database.csv')

    filtered_data = FilterAge(filtered_data, 20, 25)

    filtered_data = FilterNationality(filtered_data, "germany")

    filtered_data = FilterCountryOfResidence(filtered_data, "germany")

    filtered_data = FilterGPA(filtered_data, 8.0, 10.0)

    filtered_data = FilterAvailability(filtered_data, 10)

    filtered_data = FilterGraduationYear(filtered_data, 2028)

    return(filtered_data)

