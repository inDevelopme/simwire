from flask import Flask, jsonify, request
from .env_load import Config
from flask_cors import CORS
from flask_login import LoginManager
from .blueprints import home_bp, auth_bp, admin_bp
from .models import db, migrate
from .models import User
from flask import request, jsonify

app = Flask(__name__, template_folder='templates')
CORS(app)


config = Config()
config.get_environment_config()
config.set_server_side_session(db)

# sqlalchemy needs to know the database configuration
app.config.from_object(config)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# initialize sqlalchemy
db.init_app(app)
migrate.init_app(app, db)


# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id: int):
    # Replace this with your logic for loading users from a database
    return User.query.get(user_id)

# this makes sure that we exclude health checks in the SQL session management
@app.before_request
def exclude_health_check_routes():
    if request.path.startswith('/health_check'):
        try:
            return jsonify(status='ok')
        except (TypeError, ValueError) as e:
            # Handle any exceptions that may occur during the health check
            return jsonify(status='error', message='error'), 500  # Return a 500 Internal Server Error on failure


# aws uses this route to check that the site is operational
@app.route('/health_check')
def health_check():
    # Minimal health check logic here (e.g., check database connection)
    try:
        # Perform a minimal check (e.g., check the database connection)
        # If using SQLAlchemy, roll back any uncommitted transactions to avoid session creation
        return jsonify(status='ok')
    except (TypeError, ValueError) as e:
        # Handle any exceptions that may occur during the health check
        return jsonify(status='error', message='error'), 500  # Return a 500 Internal Server Error on failure


# this makes the app aware of the modules that need to be loaded
app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

