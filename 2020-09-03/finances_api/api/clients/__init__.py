# The finances Blueprint handles the finances management for this application
from flask import Blueprint
clients_blueprint = Blueprint('clients', __name__)

from . import controllers
