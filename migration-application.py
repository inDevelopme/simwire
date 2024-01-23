# TODO: Need to figure out how to get rid of this.
# Until then, only use this to run the command for flask migrations
from flask import Flask
# The removal of the relative path is the solution to removing the codebase
from .simwire_plugin.env_load import Config
from flask_cors import CORS
from .simwire_plugin.blueprints import home_bp, auth_bp, admin_bp
from .simwire_plugin.models import db, migrate

app = Flask(__name__)
CORS(app)

config = Config()
config.get_environment_config()
config.set_server_side_session(db)

# sqlalchemy needs to know the database configuration
app.config.from_object(config)

# initialize sqlalchemy
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    app.debug = True
    app.run()
