from flask import Blueprint

pages = Blueprint('db', __name__)

from . import views