from flask import render_template
from . import users
from app.users.models import User


@users.route('/')
def index():
    return render_template('users/index.html',
                           title="Users",
                           users=User.get_all_users(User()))
