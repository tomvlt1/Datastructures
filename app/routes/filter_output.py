from flask import Blueprint, render_template, request

collaborators_bp = Blueprint('collaborators', __name__)

@collaborators_bp.route('/')
def collaborators():
    filtered_data = data
    return render_template('collaborators.html', tables=filtered_data.to_html(classes='table table-striped table-bordered', index=False)) #boostrapframwork for display, no index displayed

@collaborators_bp.route('/filter', methods=['POST']) #only when the form is submitted
def filter_data():
    filtered_data = data

    # Get filter values from form
    age_range = request.form.get('age_range')
    if age_range:
        age_range = age_range.split(',')
        min_age = int(age_range[0])
        max_age = int(age_range[1])
        filtered_data = FilterAge(filtered_data, min_age, max_age)

    gpa_range = request.form.get('gpa_range')
    if gpa_range:
        gpa_range = gpa_range.split(',')
        min_gpa = float(gpa_range[0])
        max_gpa = float(gpa_range[1])
        filtered_data = FilterGPA(filtered_data, min_gpa, max_gpa)

    availability_range = request.form.get('availability_range')
    if availability_range:
        availability_range = availability_range.split(',')
        min_hours = int(availability_range[0])
        max_hours = int(availability_range[1])
        filtered_data = FilterAvailability(filtered_data, min_hours, max_hours)

    nationality = request.form.get('nationality')
    country_of_residence = request.form.get('country_of_residence')
    degree = request.form.get('degree')
    graduation_year = request.form.get('graduation_year', type=int)
    looking_for = request.form.get('looking_for')

    # Apply filters
    filtered_data = FilterNationality(filtered_data, nationality)
    filtered_data = FilterCountryOfResidence(filtered_data, country_of_residence)
    filtered_data = FilterDegree(filtered_data, degree)
    filtered_data = FilterGraduationYear(filtered_data, graduation_year)
    filtered_data = FilterLookingFor(filtered_data, looking_for)

    # Convert filtered data to HTML
    if filtered_data.empty:
        filtered_data_html = "<p>No results found matching your criteria.</p>"
    else:
        filtered_data_html = filtered_data.to_html(classes='table table-striped table-bordered', index=False)
    return render_template('filter_results.html', tables=filtered_data_html)


