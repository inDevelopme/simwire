from flask import render_template, url_for, redirect
from flask_login import LoginManager, login_required, current_user, logout_user, login_user
from flask import Flask, render_template, jsonify, request, flash, url_for, redirect
from pathlib import Path
from passlib.exc import MalformedHashError, InvalidHashError
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import NoResultFound, MultipleResultsFound, SQLAlchemyError

from . import auth_bp
from models import User


def load_user(username: str):
    try:
        user: User = User.query.filter_by(username=username).first()
    except NoResultFound:
        user = None
    except MultipleResultsFound:
        # Handle the case where multiple users with the same username are found
        # This should not be possible but still want to cover for it because the exception is possible.
        raise Exception("Multiple users found with the same username")
    except SQLAlchemyError as e:
        # Handle other SQLAlchemy errors
        print(f"error occurred: {e}")
        user = None

    return user


def hash_password(password):
    # Hash the password using PBKDF2
    return pbkdf2_sha256.hash(password)


def verify_password(username, password, hashed_password):
    match_found = False
    try:
        match_found = pbkdf2_sha256.verify(password, hashed_password)
    except (MalformedHashError, InvalidHashError) as e:
        print(f"Malformed / Invalid Hash Error when verifying password for {username}")
    except ValueError as e:
        print(f"Unexpected error when validating password for {username}")
    return match_found


# renders the manual login page
@auth_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


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
    return render_template('logout.html')

