from flask import render_template
from flask_login import login_required

from app.comments.models import Comment
from app.pages.models import Page
from app.tags.models import Tag
from . import dashboard


@dashboard.route('/')
def index():
    return render_template('dashboard/index.html',
                           title="Dashboard",
                           pages=Page.get_recent(Page(), 5),
                           comments=Comment.recent_comments(Comment(), 5),
                           tags=Tag.popular_tags(Tag(), 5))
