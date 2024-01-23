from flask import Flask, jsonify, request
from simwire_plugin.env_load import Config
from flask_cors import CORS
from pathlib import Path
from flask_login import LoginManager
from simwire_plugin.blueprints import home_bp, auth_bp, admin_bp
from simwire_plugin.models import db, migrate
from simwire_plugin.models.user import User

app = Flask(__name__, template_folder='simwire_plugin/templates')
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


@app.before_request
def exclude_health_check_routes():
    if request.path.startswith('/health_check'):
        try:
            return jsonify(status='ok')
        except (TypeError, ValueError) as e:
            # Handle any exceptions that may occur during the health check
            return jsonify(status='error', message='error'), 500  # Return a 500 Internal Server Error on failure


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


app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
