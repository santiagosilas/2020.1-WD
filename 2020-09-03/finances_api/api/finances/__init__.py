# The finances Blueprint handles the finances management for this application
from flask import Blueprint
finances_blueprint = Blueprint('finances', __name__)

from . import controllers
