from flask import render_template
from . import database
from app.pages.models import Page
from app.users.models import User
from app.comments.models import Comment
from app.tags.models import Tag


@database.route('/')
def index():
    return render_template('database/index.html',
                           title="Database",
                           users=User.all(User()),
                           pages=Page.get_all_pages(Page()),
                           comments=Comment.get_all_comments(Comment()),
                           tags=Tag.get_all_tags(Tag()))
