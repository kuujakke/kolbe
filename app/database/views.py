from flask import render_template
from . import database
from app import models


@database.route('/')
def index():

    return render_template('database/index.html',
                           title="Database",
                           users=models.get_all_users(),
                           pages=models.get_all_pages(),
                           comments=models.get_all_comments(),
                           tags=models.get_all_tags())
