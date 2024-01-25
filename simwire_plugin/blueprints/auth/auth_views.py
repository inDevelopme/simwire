from flask_login import login_required, current_user, logout_user, login_user
from flask import render_template, request, flash, url_for, redirect
from simwire_plugin.blueprints.auth.auth_dao import User, load_user
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
    return f"Welcome, {current_user.id}! This is a protected page." + str(url_for('auth.landing_page'))


@auth_bp.route('/login', methods=['POST'])
def login_validate():

    if current_user.is_authenticated:
        return redirect(url_for('auth.landing_page'))

    form_username: str = request.form['username']
    form_password: str = request.form['password']

    user: User = load_user(form_username)
    password: str = form_password

    if user:
        if verify_password(user.username, password, user.password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('auth.landing_page'))

    flash('Login failed. Please check your credentials and try again.', 'danger')
    return redirect(url_for('auth.login'))


@auth_bp.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('auth_logout.html')
