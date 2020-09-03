from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Cria-se as instâncias das extensões Flask
db = SQLAlchemy()
ma = Marshmallow()

def create_api(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    # initialize extensions
    db.init_app(app)
    ma.init_app(app) 

    # register blueprints
    from api.core import core_blueprint
    from api.finances import finances_blueprint
    from api.clients import clients_blueprint
    app.register_blueprint(core_blueprint)
    app.register_blueprint(finances_blueprint)
    app.register_blueprint(clients_blueprint)

    return app
