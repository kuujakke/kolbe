from flask import render_template
from flask_login import login_required

from . import dashboard


@login_required
@dashboard.route('/')
def index():
    return render_template('dashboard/index.html', title="Dashboard")
