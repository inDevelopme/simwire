from flask_login import login_required, current_user, logout_user, login_user
from flask import render_template, request, flash, url_for, redirect, jsonify
from werkzeug.exceptions import BadRequest

from .auth_dao import User, load_user
from ..admin.admin_dblib import AdminBase
from . import verify_password
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, template_folder='templates')


# renders the manual login page
@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('auth_login.html')


# load the views
@auth_bp.route('/homepage')
@login_required
def landing_page():
    admin = AdminBase()
    u: User = admin.get_user_by_id(current_user.id)

    return f"Welcome, {current_user.id} w/ {u.username}! This is a protected page." + str(url_for('auth.landing_page'))


@auth_bp.route('/login', methods=['POST'])
def login_validate():

    form_username = ''
    form_password = ''

    # check if the user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('auth.landing_page'))

    # check if the request coming is json type
    if request.headers['Content-Type'] == 'application/json':
        try:
            # parse json data from the request
            json_data = request.json

            # Now json_data contains the parsed json
            # You can access the JSON fields like json_data['key']
            form_username: str = json_data['username']
            form_password: str = json_data['password']
        except BadRequest:
            return jsonify({'error': 'Invalid JSON data'}), 400
        except ValueError:
            return jsonify({'error': 'Error parsing JSON data'}), 400
    else:
        return jsonify({'error': 'Expected Content-Type: application-type/json'}), 400

    # now use the form data to get the user
    user: User = load_user(form_username)
    password: str = form_password

    if user:
        if verify_password(user.username, password, user.password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return '1'

    flash('Login failed. Please check your credentials and try again.', 'danger')
    return '0'


@auth_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('auth_logout.html')
