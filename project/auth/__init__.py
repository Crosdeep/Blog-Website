from flask import Blueprint, Flask

auth = Blueprint('auth', __name__, template_folder='templates')

from . import routes



