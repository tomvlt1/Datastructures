from flask import Blueprint, render_template
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

collaborators_bp = Blueprint('collaborators', __name__)


@collaborators_bp.route('/')
def collaborators():
    filtered_data = initial_data
    return render_template('collaborators.html', 
                           tables=filtered_data.to_html(classes='table table-striped table-bordered', index=False))

@collaborators_bp.route('/filter', methods=['POST'])
def datafilter():
    
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


    def Final_Sort(filtered_data):
        final_data = AddSortValue(filtered_data, GetLookingFor(), GetLookingForDegree())
        return final_data

 
    filtered_data = Filtered_Data(initial_data)
    sorted_data = Final_Sort(filtered_data)

    
    if sorted_data.empty:
        filtered_data_html = "<p>No results found matching your criteria.</p>"
    else:
        filtered_data_html = sorted_data.to_html(classes='table table-striped table-bordered', index=False)
    
    return render_template('results.html', tables=filtered_data_html)





