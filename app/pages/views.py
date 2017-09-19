from flask import render_template
from . import pages
from app import models

@pages.route('/')
def index():

    return render_template('pages/index.html',
                           title="Pages",
                           pages=models.get_all_pages())
