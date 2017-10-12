from html import escape

from flask import render_template, flash, redirect, current_app as app
from flask_login import login_required
from flask_pagedown.fields import PageDownField
from flask_wtf import Form
from wtforms.validators import DataRequired

from . import tags
from app.tags.models import Tag


@tags.route('/')
def index():
    return render_template('tags/index.html',
                           title="Tags",
                           tags=Tag.get_all_tags(Tag()),
                           form=Form(secret_key=app.config['SECRET_KEY']))


@tags.route('/new', methods=["POST", "GET"])
@login_required
def new():
    tag = Tag(('', ''))
    form = NewForm(secret_key=app.config['SECRET_KEY'], obj=tag)
    if form.validate_on_submit():
        form.populate_obj(tag)
        Tag.new_tag(tag, tag)
        flash('New tag created successfully!', 'success')
        return redirect('/tags')
    elif form.is_submitted():
        flash('The new tag can\'t be empty!', 'warning')
    return render_template('tags/new.html',
                           title="New Tag",
                           form=form)


@tags.route('/<tag_id>/edit', methods=["POST", "GET"])
@login_required
def edit(tag_id):
    tag = Tag.get_tag(Tag(), tag_id)
    form = EditForm(secret_key=app.config['SECRET_KEY'], obj=tag)
    if form.validate_on_submit():
        form.populate_obj(tag)
        tag.save_tag(tag)
        flash('Tag edited successfully.', 'success')
        return redirect('/tags')
    elif form.is_submitted():
        flash('Can\'t submit empty tag!', 'warning')
    return render_template('tags/edit.html',
                           title="Edit Tag",
                           form=form)


@tags.route('/<tag_id>/delete', methods=["POST"])
@login_required
def delete(tag_id):
    print(tag_id)
    Tag.delete_tag(Tag(), Tag((tag_id, '')))
    flash('Tag deleted successfully!', 'success')
    return redirect('/tags')


def sanitize_field(form, field):
    field.data = escape(field.data)


class EditForm(Form):
    content = PageDownField('content', validators=[DataRequired(), sanitize_field])


class NewForm(Form):
    content = PageDownField('content', validators=[DataRequired(), sanitize_field])
