﻿# coding: utf-8
from flask import Flask

app = Flask(__name__)
app.debug = True

from api import routes