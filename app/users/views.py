from flask import flash, render_template, redirect, current_app
from flask_login import login_user, login_required, logout_user, current_user
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from app.users.redirectForm import RedirectForm
from . import users
from app.users.models import User


@login_required
@users.route('/')
def index():
    return render_template('users/index.html',
                           title="Users",
                           users=User.all(User()))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.verify(User(), form.email.data, form.password.data)
        if user is not None:
            if login_user(user):
                current_app.logger.debug('%s has logged in', user.email)
                flash('Logged in successfully.')
                return form.redirect('/')
        flash('Wrong email or password.')
        error = "Wrong email or password."
    return render_template('users/login.html', form=form, error=error)


@login_required
@users.route('/logout')
def logout():
    current_app.logger.debug('%s has logged out', current_user.email)
    logout_user()
    return redirect('/')


@login_required
@users.route('/profile')
def profile():
    pass


class LoginForm(RedirectForm):
    email = StringField('Email', validators=[DataRequired(), Length(6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])