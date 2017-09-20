from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_login import LoginManager
from flask_wtf.csrf import CsrfProtect
from flask_pagedown import PageDown

from config import app_config

login_manager = LoginManager()
csrf = CsrfProtect()

nav = Nav()

@nav.navigation()
def navbar():
    return Navbar(
        'kolbe',
        View('Dashboard', 'dashboard.index'),
        View('Pages', 'pages.index'),
        #View('Tags', 'tags'),
        #View('Users', 'users'),
        View('Database', 'database.index'),
    )

def create_app(config_name):
    application = Flask(__name__)
    application.config.from_object(app_config[config_name])
    application.config.from_pyfile('../config.py')

    Bootstrap(application)
    nav.init_app(application)
    csrf.init_app(application)
    pagedown = PageDown(application)

    login_manager.init_app(application)
    login_manager.login_message = "Login to access this page"
    login_manager.login_view = "auth.login"



    from .pages import pages as pages_blueprint
    application.register_blueprint(pages_blueprint, url_prefix='/pages')

    from .database import database as database_blueprint
    application.register_blueprint(database_blueprint, url_prefix='/database')

    from .dashboard import dashboard as dashboard_blueprint
    application.register_blueprint(dashboard_blueprint, url_prefix='/')

    return application
