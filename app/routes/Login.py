import hashlib
import csv
from flask import Blueprint, render_template, request, redirect, session, url_for
from userclass import User  # Class user.py

login_bp = Blueprint('login', __name__)

# Route for login page
@login_bp.route('/')
def login_page():
    return render_template('login.html')

# Route to process login
@login_bp.route('/submit_login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    # Load user data from CSV
    user_data = User.load_user_data()

    # Verify email in loaded data
    for user in user_data:
        if user['email'] == email:
            # Compare hashed password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user['password'] == hashed_password:
                session['IsLogged'] = True
                session['email'] = email  # Save email in session
                return redirect(url_for('home.home'))  # Redirect after successful login

    # If user not found or password is incorrect
    session['IsLogged'] = False
    session['email'] = ''
    error_message = "Invalid login credentials. Please check your email and password."
    return render_template('login.html', error_message=error_message)

# Route for user registration page
@login_bp.route('/registerPage')
def register_page():
    return render_template('registerPage.html')

# Route to register a new user
@login_bp.route('/register', methods=['POST'])
def register():
    # Get form data
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    description = request.form['description']
    additional_info = request.form['additional_info']
    rating = request.form.get('rating')  # Optional
    age = request.form['age']
    dob = request.form['dob']
    nationality = request.form['nationality']
    country_residence = request.form['country_residence']
    degree = request.form['degree_studied']
    graduation_year = request.form['graduation_year']
    gpa = request.form.get('gpa')  # Optional
    availability = request.form['availability']
    topics_of_interest = request.form['fields_of_expertise']
    user_type = request.form['user_type']
    linkedin = request.form['linkedin']

    # Create User object
    user = User(
        first_name, last_name, email, password, description, additional_info, rating,
        age, dob, nationality, country_residence, degree, graduation_year, gpa,
        availability, topics_of_interest, user_type, linkedin
    )

    # Validate user data
    if not user.validate_email():
        error_message = "Invalid email format"
        return render_template('registerPage.html', error_message=error_message)

    if not user.validate_password():
        error_message = "Password must be at least 8 characters long, with at least one uppercase letter, one number, and one special character"
        return render_template('registerPage.html', error_message=error_message)

    if not user.validate_age():
        error_message = "Age must be between 18 and 120"
        return render_template('registerPage.html', error_message=error_message)

    if not user.validate_dob():
        error_message = "Invalid date format for Date of Birth. Use YYYY-MM-DD"
        return render_template('registerPage.html', error_message=error_message)

    if not user.validate_linkedin():
        error_message = "Invalid LinkedIn URL format"
        return render_template('registerPage.html', error_message=error_message)

    # Check if email is already registered
    if User.email_exists(email):
        error_message = "Email already registered"
        return render_template('registerPage.html', error_message=error_message)

    # Save new user to CSV
    user.save_to_csv()

    return redirect(url_for('login.login_page'))

# Function to save data to CSV
def save_to_csv(
    first_name, last_name, rating, age, dob, nationality, country_residence,
    degree, graduation_year, gpa, availability, topics_of_interest, email,
    description, additional_info, sort_value, user_type, hashed_password, linkedin
):
    fieldnames = [
        'First Name', 'Last Name', 'Rating', 'Age', 'DOB', 'Nationality', 
        'Country of Residence', 'Degree', 'Graduation Year', 'GPA', 'Availability',
        'Topics of Interest', 'Email', 'Description', 'Additional Information', 
        'Sort Value', 'Type', 'Password', 'LinkedIn'
    ]

    with open('generated_database.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header if the file is empty
        if file.tell() == 0:
            writer.writeheader()

        # Write data
        writer.writerow({
            'First Name': first_name,
            'Last Name': last_name,
            'Rating': rating,
            'Age': age,
            'DOB': dob,
            'Nationality': nationality,
            'Country of Residence': country_residence,
            'Degree': degree,
            'Graduation Year': graduation_year,
            'GPA': gpa,
            'Availability': availability,
            'Topics of Interest': topics_of_interest,
            'Email': email,
            'Description': description,
            'Additional Information': additional_info,
            'Sort Value': sort_value,
            'Type': user_type,
            'Password': hashed_password,
            'LinkedIn': linkedin
        })
