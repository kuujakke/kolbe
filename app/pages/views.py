from flask import current_app as app, render_template, redirect
from . import pages
from app import models
from flask_wtf import Form
from wtforms import HiddenField, TextAreaField
from wtforms.validators import DataRequired


@pages.route('/')
def index():
    return render_template('pages/index.html',
                           title="Pages",
                           pages=models.get_all_pages())


@pages.route('/new')
def new():
    return render_template('pages/new.html',
                           title="New Page")


@pages.route('/<id>/edit', methods=["POST", "GET"])
def edit(id):
    page = models.get_page_by_id(id)
    form = EditForm(secret_key=app.config['SECRET_KEY'], obj=page)
    if form.validate_on_submit():
        form.populate_obj(page)
        models.save_page_content(page)
        return redirect('/pages')
    return render_template('pages/edit.html',
                           title="Edit Page",
                           form=form)


class EditForm(Form):
    user_id = HiddenField('user_id', validators=[DataRequired()])
    content = TextAreaField('content', validators=[DataRequired()])



