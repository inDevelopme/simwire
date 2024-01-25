from flask import render_template
from flask import Blueprint

home_bp = Blueprint('home', __name__)
@home_bp.route('/')
def index():
    return render_template('homepage.html')
