from flask import render_template, request, redirect, Blueprint
import hashlib
import csv

login_bp = Blueprint('login', __name__)
user_data = {}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/submit_login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email in user_data:
        hashed_password = hash_password(password)
        if user_data[email] == hashed_password:
            return redirect('/home')  
    return "Invalid login credentials"

@app.route('/registerPage')
def register_page():
    return render_template('registerPage.html')

@app.route('/submit_registration', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    description = request.form['description']
    additional_info = request.form['additional_info']
    
    hashed_password = hash_password(password)

    save_to_csv(first_name, last_name, email, description, additional_info)

    user_data[email] = hashed_password
    
    return redirect('/')

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_to_csv(first_name, last_name, email, description, additional_info):
    with open('generated_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, '', '', '', '', '', '', '', '', '', email, description, additional_info])

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)