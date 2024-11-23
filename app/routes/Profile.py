from flask import render_template, request, redirect, Blueprint


account_bp = Blueprint('account', __name__)
user_data = {}

@account_bp.route('/')
def account_page():
    return render_template('profile.html')

