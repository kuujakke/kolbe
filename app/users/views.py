from flask import flash, render_template
from flask_login import login_user
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from app.users.redirectForm import RedirectForm
from . import users
from app.users.models import User


@users.route('/')
def index():
    return render_template('users/index.html',
                           title="Users",
                           users=User.all(User()))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_email(User(), form.email.data)
        if user:
            login_user(user)
            flash('Logged in successfully.')
        return form.redirect('/dashboard')
    else:
        flash('Wrong email or password.')

    return render_template('users/login.html', form=form)


@users.route('/logout')
def logout():
    pass


@users.route('/profile')
def profile():
    pass


class LoginForm(RedirectForm):
    email = StringField('Email', validators=[DataRequired(), Length(6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])
