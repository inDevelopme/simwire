# TODO: Need to figure out how to get rid of this.
# Until then, only use this to run the command for flask migrations
from flask import Flask
# The removal of the relative path is the solution to removing the codebase
from .simwire_plugin.env_load import Config
from .simwire_plugin.models import db, migrate

app = Flask(__name__)

config = Config()
config.get_environment_config()
config.set_server_side_session(db)

# sqlalchemy needs to know the database configuration
app.config.from_object(config)

# initialize sqlalchemy
db.init_app(app)
migrate.init_app(app, db)

