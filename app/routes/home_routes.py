# this file defines a blueprint for the home page
# it serves the main landing page of our application

from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('home.html')
