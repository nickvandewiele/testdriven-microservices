# users-service/project/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

# instantiate db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()

def create_app():

	# instantiate the app
	app = Flask(__name__)

	# set config
	app_settings = os.getenv('APP_SETTINGS')
	app.config.from_object(app_settings)

	# set up extensions
	db.init_app(app)
	toolbar.init_app(app)

	# register blueprints
	from project.api.users import users_blueprint
	app.register_blueprint(users_blueprint)

	return app
	