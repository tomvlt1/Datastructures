import hashlib
from flask import Blueprint, render_template, request, redirect, session, url_for
from userclass import User 
from datetime import datetime
from validation import  validation_function

login_bp = Blueprint('login', __name__)

@login_bp.route('/login_page')
def login_page():
    return render_template('login.html')

@login_bp.route('/submit_login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user_data = User.load_all_user_data()

    # Verify email and password 
    for user in user_data:
        if user['Email'].lower() == email.lower():
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user['Password'] == hashed_password:
                session['IsLogged'] = True #session variables that are saved for all the pages.
                session['email'] = email.lower() 
                return redirect(url_for('account.account_page'))  # redirects, is like render_template of the profile page. 
    # If user not found or password is incorrect, dont reach the return
    session['IsLogged'] = False
    session['email'] = ''
    error_message = "Invalid login credentials. Please check your email and password."
    return render_template('login.html', error_message=error_message)

# Route to register a new user
@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
    # Get form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        description = request.form.get('description')
        additional_info = request.form.get('additional_info')
        age = request.form.get('age') 
        dob = request.form.get('dob')
        nationality = request.form.get('nationality')
        country_residence = request.form.get('country_residence')
        degree = request.form.get('degree_studied')
        graduation_year = request.form.get('graduation_year')
        gpa = request.form.get('gpa')  
        availability = request.form.get('availability')
        topics_of_interest = request.form.get('fields_of_expertise')
        user_type = request.form.get('user_type')
        linkedin = request.form.get('linkedin')
        mentor = request.form.get('mentor') 
        
        #datatype date to calculate the age
        birthdate=datetime.strptime(dob, "%Y-%m-%d") 
        today = datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        age = int(age)
        
        # If mentor is not checked, set it to False, otherwise True
        if mentor:
            mentor = True
        else:
            mentor = False
            
        image=''
        rating=0

        # Create User object
        user = User(first_name, last_name, email, password, description, additional_info, rating,
            age, dob, nationality, country_residence, degree, graduation_year, gpa,
            availability, topics_of_interest, user_type, linkedin,mentor,image)   
        # Validate user data
        vValid,verr= validation_function(user,0)
        
        if vValid==1:
            return render_template('registerPage.html', error_message=verr)
        else:   
        # Save new user to CSV
            User.save_to_csv(user)
            return redirect(url_for('login.login_page'))
    else:
        return render_template('registerPage.html')

