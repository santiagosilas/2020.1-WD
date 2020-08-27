# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
#app.config['DEBUG'] = ..
#app.config.debug = ...

db = SQLAlchemy(app)
ma = Marshmallow(app)



from api import models, utils
from api.controllers import user_controller
from api.controllers import task_controller
from api.controllers import default_controller