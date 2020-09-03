# The finances Blueprint handles the finances management for this application
from flask import Blueprint
core_blueprint = Blueprint('core', __name__, template_folder='templates') 

from . import controllers
