from flask import flash, render_template, redirect, current_app
from flask_login import login_user, login_required, logout_user, current_user
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from . import users
from app.users.models import User


@users.route('/')
@login_required
def index():
    return render_template('users/index.html',
                           title="Users",
                           users=User.all(User()))


@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(secret_key=current_app.config['SECRET_KEY'])
    error = None
    if form.validate_on_submit():
        user = User.verify(User(), form.email.data, form.password.data)
        if user is not None and login_user(user):
            current_app.logger.debug('%s has logged in', user.email)
            flash('Logged in successfully.', 'success')
            return redirect('/')
        flash('Wrong email or password.', 'danger')
    elif form.is_submitted():
        flash('Make sure both fields contain something!', 'warning')
    return render_template('users/login.html', form=form, error=error)


@users.route('/logout')
@login_required
def logout():
    current_app.logger.debug('%s has logged out', current_user.email)
    flash('Logged out', 'info')
    logout_user()
    return redirect('/')


@users.route('/profile')
@login_required
def profile():
    pass


class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8)])