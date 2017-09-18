from flask import render_template
from . import database
from app import models


@database.route('/')
def index():

    return render_template('database/index.html',
                           title="Database",
                           users=models.get_users(),
                           pages=models.get_pages(),
                           comments=models.get_comments(),
                           tags=models.get_tags())
