from flask import current_app as app, render_template, redirect, Markup, flash
from flask_login import login_required, current_user

from . import pages
from app.comments.models import Comment
from app.pages.models import Page
from flask_wtf import Form
from wtforms import HiddenField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField
import markdown


@pages.route('/')
def index():
    return render_template('pages/index.html',
                           title="Pages",
                           pages=Page.get_all_pages(Page()))


@pages.route('/new', methods=["POST", "GET"])
@login_required
def new():
    page = Page(('', current_user.user_id, ''))
    form = NewForm(secret_key=app.config['SECRET_KEY'], obj=page)
    if form.validate_on_submit():
        form.populate_obj(page)
        Page.new_page(page, page)
        flash('New page created successfully!', 'success')
        return redirect('/pages')
    elif form.is_submitted():
        flash('The new page can\'t be empty!', 'warning')
    return render_template('pages/new.html',
                           title="New Page",
                           form=form)


@pages.route('/<page_id>', methods=["POST", "GET"])
def show(page_id):
    page = Page.get_page(Page(), page_id)
    form = CommentForm(secret_key=app.config['SECRET_KEY'])
    content = Markup(markdown.markdown(page.content))
    comments = process_comments(page.get_comments())
    comment = Comment(('', current_user.user_id, page_id, ''))
    print(form.content)
    if form.validate_on_submit():
        form.populate_obj(comment)
        comment.save_comment()
        flash('Comment posted successfully!', 'success')
        return redirect('/pages/%s' % page_id)
    elif form.is_submitted():
        flash('Can\'t post if there is no content!', 'warning')
    return render_template('pages/show.html',
                           title="Show Page",
                           content=content,
                           page_id=page_id,
                           comments=comments,
                           comment=comment,
                           form=form)


@pages.route('/<page_id>/edit', methods=["POST", "GET"])
@login_required
def edit(page_id):
    page = Page.get_page(Page(), page_id)
    form = EditForm(secret_key=app.config['SECRET_KEY'], obj=page)
    if form.validate_on_submit():
        form.populate_obj(page)
        page.save_page()
        flash('Page edited successfully.', 'success')
        return redirect('/pages/%s' % page_id)
    elif form.is_submitted():
        flash('Can\'t submit empty page!', 'warning')
    return render_template('pages/edit.html',
                           title="Edit Page",
                           form=form)


@pages.route('/<page_id>/delete', methods=["POST"])
@login_required
def delete(page_id):
    Page.delete_page(Page((page_id, '', '')))
    flash('Page deleted successfully!', 'success')
    return redirect('/pages')


def process_comments(comments):
    if comments:
        for comment in comments:
            comment.content = Markup(markdown.markdown(comment.content))
    return comments


class EditForm(Form):
    user_id = HiddenField('user_id', validators=[DataRequired()])
    content = PageDownField('content', validators=[DataRequired()])


class NewForm(EditForm):
    user_id = HiddenField('user_id', validators=[DataRequired()])
    content = PageDownField('content', validators=[DataRequired()])


class CommentForm(Form):
    user_id = HiddenField('user_id', validators=[DataRequired()])
    content = PageDownField('content', validators=[DataRequired()])
