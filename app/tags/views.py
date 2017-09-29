from flask import render_template
from . import tags
from app.tags.models import Tag


@tags.route('/')
def index():
    return render_template('tags/index.html',
                           title="Tags",
                           tags=Tag.get_all_tags(Tag()))
