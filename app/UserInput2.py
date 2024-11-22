from flask import request

def GetAge(age_range=None):
    if age_range is None:  # Si no se proporciona directamente, usa request
        age_range = request.form.get('age_range')
    if age_range:
        age_range = age_range.split(',')
        min_age = int(age_range[0])
        max_age = int(age_range[1])
        return min_age, max_age
    return None, None

def GetGPA(gpa_range=None):
    if gpa_range is None:  # Si no se proporciona directamente, usa request
        gpa_range = request.form.get('gpa_range')
    if gpa_range:
        gpa_range = gpa_range.split(',')
        min_gpa = float(gpa_range[0])
        max_gpa = float(gpa_range[1])
        return min_gpa, max_gpa
    return None, None

def GetAvailability(availability_range=None):
    if availability_range is None:  # Si no se proporciona directamente, usa request
        availability_range = request.form.get('availability_range')
    if availability_range:
        availability_range = availability_range.split(',')
        min_hours = int(availability_range[0])
        max_hours = int(availability_range[1])
        return min_hours, max_hours
    return None, None

def GetNationality(nationality=None):
    if nationality is None:  # Si no se proporciona directamente, usa request
        nationality = request.form.get('nationality')
    return nationality

def GetCountryOfResidence(country_of_residence=None):
    if country_of_residence is None:  # Si no se proporciona directamente, usa request
        country_of_residence = request.form.get('country_of_residence')
    return country_of_residence

def GetDegree(degree=None):
    if degree is None:  # Si no se proporciona directamente, usa request
        degree = request.form.get('degree')
    return degree

def GetGraduationYear(graduation_year=None):
    if graduation_year is None:  # Si no se proporciona directamente, usa request
        graduation_year = request.form.get('graduation_year', type=int)
    return graduation_year

def GetLookingFor(looking_for=None):
    if looking_for is None:  # Si no se proporciona directamente, usa request
        looking_for = request.form.get('looking_for')
    if looking_for:
        looking_for_list = [item.strip() for item in looking_for.split(',')]
        return looking_for_list
    return []  

def GetLookingForDegree(degree=None):
    if degree is None:  # Si no se proporciona directamente, usa request
        degree = request.form.get('degree')
    if degree:
        degree_list = [item.strip() for item in degree.split(',')]
        return degree_list
    return []



