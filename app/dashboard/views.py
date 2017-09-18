from flask import render_template
from . import dashboard

@dashboard.route('/')
def index():
    return render_template('dashboard/index.html', title="Dashboard")
