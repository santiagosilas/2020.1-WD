from flask import Flask, jsonify, request, abort, make_response
from api import app

@app.route('/')
def home():
    return 'my flask api'

@app.errorhandler(404)
def not_found(error):
    print('error', error)
    #return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'error': 'Not found'}), 404