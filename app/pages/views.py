from flask import current_app as app, render_template, redirect, Markup
from . import pages
from app import models
from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField
import markdown


@pages.route('/')
def index():
    return render_template('pages/index.html',
                           title="Pages",
                           pages=models.get_all_pages())


@pages.route('/new', methods=["POST", "GET"])
def new():
    user_id = 1
    page = models.Page(('', user_id, ''))
    form = NewForm(secret_key=app.config['SECRET_KEY'], obj=page)
    if form.validate_on_submit():
        form.populate_obj(page)
        models.new_page(page)
        return redirect('/pages')
    return render_template('pages/new.html',
                           title="New Page",
                           form=form)


@pages.route('/<page_id>')
def show(page_id):
    page = models.get_page(models.Page((page_id, '', '')))
    content = Markup(markdown.markdown(page.content))
    return render_template('pages/show.html',
                           title="Show Page",
                           content=content,
                           page_id=page_id,
                           form=Form(secret_key=app.config['SECRET_KEY']))


@pages.route('/<page_id>/edit', methods=["POST", "GET"])
def edit(page_id):
    page = models.get_page(models.Page((page_id, '', '')))
    form = EditForm(secret_key=app.config['SECRET_KEY'], obj=page)
    if form.validate_on_submit():
        form.populate_obj(page)
        models.save_page(page)
        return redirect('/pages/%s' % page_id)
    return render_template('pages/edit.html',
                           title="Edit Page",
                           form=form)

@pages.route('/<page_id>/delete', methods=["POST"])
def delete(page_id):
    models.delete_page(page_id)
    return redirect('/pages')


class EditForm(Form):
    user_id = HiddenField('user_id', validators=[DataRequired()])
    content = PageDownField('content', validators=[DataRequired()])


class NewForm(EditForm):
    user_id = HiddenField('user_id', validators=[DataRequired()])
    content = PageDownField('content', validators=[DataRequired()])
