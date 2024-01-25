from flask_login import login_required
from flask import render_template
from flask import Blueprint
admin_bp = Blueprint('admin', __name__, template_folder='templates')


@admin_bp.route('/admin')
@login_required
def admin_landing_page():
    return render_template('administration.html')