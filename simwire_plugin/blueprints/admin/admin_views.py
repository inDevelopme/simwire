from flask_login import login_required, current_user
from flask import render_template
from flask import Blueprint
from .admin_dblib import AdminBase

admin_bp = Blueprint('admin', __name__, template_folder='templates')


@admin_bp.route('/admin')
@login_required
def admin_landing_page():
    admin = AdminBase()
    u = admin.get_user_by_id(current_user.id)
    data_dict = dict()
    data_dict['test'] = 'test'
    data_dict['user'] = u.username
    return render_template('administration.html', template_data=data_dict)
