from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the CSV file
data = pd.read_csv("generated_database.csv", header=None, names=[
    "First_name", "Last_name", "Age", "Nationality", "Country_of_residence", 
    "Degree", "Graduation_year", "GPA", "Availability", "Looking_for", 
    "Email", "Description", "Additional_information"
])

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
data['GPA'] = pd.to_numeric(data['GPA'], errors='coerce')
data['Availability'] = pd.to_numeric(data['Availability'], errors='coerce')

# Filtering functions
def FilterAge(data, min_age, max_age):
    if min_age is not None and min_age >= 0:
        data = data[data['Age'] >= min_age]
    if max_age is not None and max_age >= 0:
        data = data[data['Age'] <= max_age]
    return data

def FilterNationality(data, nationality):
    if nationality:
        return data[data['Nationality'].str.lower() == nationality.lower()]
    return data

def FilterCountryOfResidence(data, country):
    if country:
        return data[data['Country_of_residence'].str.lower() == country.lower()]
    return data

def FilterDegree(data, degree):
    if degree:
        return data[data['Degree'].str.lower() == degree.lower()]
    return data

def FilterGraduationYear(data, year):
    if year:
        return data[data['Graduation_year'] == year]
    return data

def FilterGPA(data, min_gpa, max_gpa):
    if min_gpa is not None and min_gpa >= 0:
        data = data[data['GPA'] >= min_gpa]
    if max_gpa is not None and max_gpa >= 0:
        data = data[data['GPA'] <= max_gpa]
    return data

def FilterAvailability(data, min_hours, max_hours):
    if min_hours is not None and min_hours >= 0:
        data = data[data['Availability'] >= min_hours]
    if max_hours is not None and max_hours >= 0:
        data = data[data['Availability'] <= max_hours]
    return data

def FilterLookingFor(data, looking_for):
    if looking_for:
        return data[data['Looking_for'].str.lower() == looking_for.lower()]
    return data

@app.route('/')
def index():
    filtered_data = data
    return render_template('filter_results.html', tables=filtered_data.to_html(classes='table table-striped table-bordered', index=False))

@app.route('/filter', methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)
