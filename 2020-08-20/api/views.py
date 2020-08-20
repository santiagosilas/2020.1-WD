# exemplo
from flask import Flask
from api import app

@app.route('/')
def home():
    return 'my flask api'
