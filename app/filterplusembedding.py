from LoadData import data as initial_data
from Filter import (
    FilterAge,
    FilterNationality,
    FilterCountryOfResidence,
    FilterDegree,
    FilterGPA,
    FilterAvailability,
    FilterGraduationYear
)
from UserInput2 import (
    GetAge,
    GetGPA,
    GetAvailability,
    GetNationality,
    GetCountryOfResidence,
    GetDegree,
    GetGraduationYear,
    GetLookingFor,
    GetLookingForDegree
)

from Display import AddSortValue 

min_age, max_age = GetAge()
min_gpa, max_gpa = GetGPA()
min_hours, max_hours = GetAvailability()
nationality = GetNationality()
country_of_residence = GetCountryOfResidence()
degree = GetDegree()
graduation_year = GetGraduationYear()

def Filtered_Data(data):
    filtered_data = data
    if min_age is not None and max_age is not None:
        filtered_data = FilterAge(filtered_data, min_age, max_age)
    if min_gpa is not None and max_gpa is not None:
        filtered_data = FilterGPA(filtered_data, min_gpa, max_gpa)
    if min_hours is not None and max_hours is not None:
        filtered_data = FilterAvailability(filtered_data, min_hours, max_hours)
    if nationality:
        filtered_data = FilterNationality(filtered_data, nationality)
    if country_of_residence:
        filtered_data = FilterCountryOfResidence(filtered_data, country_of_residence)
    if degree:
        filtered_data = FilterDegree(filtered_data, degree)
    if graduation_year:
        filtered_data = FilterGraduationYear(filtered_data, graduation_year)

    return filtered_data

def Final_Sort():
    final_data = AddSortValue(Filtered_Data(initial_data),GetLookingFor(),GetLookingForDegree())
    return final_data

