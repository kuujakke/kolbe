from flask import Flask
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CsrfProtect
from flask_pagedown import PageDown
from app.users.models import User

from config import app_config

login_manager = LoginManager()
csrf = CsrfProtect()

nav = Nav()

@nav.navigation()
def navbar():
    if current_user.is_authenticated:
        return Navbar('kolbe',
            View('Dashboard', 'dashboard.index'),
            View('Pages', 'pages.index'),
            View('Tags', 'tags.index'),
            View('Users', 'users.index'),
            View('Database', 'database.index'),
            Subgroup(current_user.email,
                     View('Profile', 'users.profile'),
                     View('Logout', 'users.logout'))
        )
    else:
        return Navbar(
            'kolbe',
            View('Pages', 'pages.index'),
            View('Tags', 'tags.index'),
            View('Login', 'users.login')
        )


@login_manager.user_loader
def load_user(user_id):
    return User.get(User(), user_id)


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

    from .users import users as users_blueprint
    application.register_blueprint(users_blueprint, url_prefix='/users')

    from .tags import tags as tags_blueprint
    application.register_blueprint(tags_blueprint, url_prefix='/tags')

    from .database import database as database_blueprint
    application.register_blueprint(database_blueprint, url_prefix='/database')

    from .dashboard import dashboard as dashboard_blueprint
    application.register_blueprint(dashboard_blueprint, url_prefix='/')


    return application
