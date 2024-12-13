# This script starts a Flask web application. It imports and registers different route blueprints 
# (home, collaborators, login, account, mentors, and projects), sets a secret key for sessions
# provides a logout function, and automatically opens the app in a web browser when it runs.
import threading
import webbrowser
import os
from flask import Flask, session, redirect, url_for
from routes.home_routes import home_bp
from routes.Collaborators_Routes import collaborators_bp
from routes.Login import login_bp
from routes.Profile import account_bp
from routes.Mentors_Routes import mentors_bp
from routes.Projects import projects_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = '456ytu@w789'

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(collaborators_bp, url_prefix='/collaborators')
app.register_blueprint(login_bp, url_prefix='/login')
app.register_blueprint(account_bp, url_prefix='/account')
app.register_blueprint(mentors_bp, url_prefix='/mentors')
app.register_blueprint(projects_bp, url_prefix='/projects')


@app.route('/logout')
def logout():
    session.clear()  
    return redirect(url_for('home.home'))  

def open_browser():
    """Open the default web browser to the app's URL."""
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        threading.Timer(1, open_browser).start()
   
    app.run(debug=True)
