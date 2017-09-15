from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_login import LoginManager

from config import app_config

login_manager = LoginManager()

nav = Nav()

@nav.navigation()
def navbar():
    return Navbar(
        'kolbe',
        #View('Home', 'index'),
        View('Pages', 'pages.index'),
        #View('Tags', 'tags'),
        #View('Users', 'users'),
        View('Database', 'db'),
    )

def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(app_config[config_name])
    application.config.from_pyfile('../config.py')
    Bootstrap(application)
    nav.init_app(application)
    login_manager.init_app(application)
    login_manager.login_message = "Login to access this page"
    login_manager.login_view = "auth.login"

    from .pages import pages as pages_blueprint
    application.register_blueprint(pages_blueprint, url_prefix='/pages')

    from .db import db as db_blueprint
    application.register_blueprint(db_blueprint, url_prefix='/database')
    return application