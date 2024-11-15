from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from form
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    nationality = request.form['nationality']
    country_of_residence = request.form['country_of_residence']
    degree = request.form['degree']
    graduation_year = request.form['graduation_year']
    gpa = request.form['gpa']
    availability = request.form['availability']
    looking_for = request.form['looking_for']
    email = request.form['email']
    description = request.form['description']
    additional_info = request.form['additional_info']

    # Save data to a CSV file
    with open('generated_database.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, age, nationality, country_of_residence, degree,
                         graduation_year, gpa, availability, looking_for, email, description, additional_info])

    return f'Thank you, {first_name}! Your data has been saved to the CSV file.'

if __name__ == '__main__':
    app.run(debug=True)
