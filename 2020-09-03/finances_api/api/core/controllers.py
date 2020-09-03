from flask import Flask, jsonify, request, abort, make_response
from . import core_blueprint

@core_blueprint.errorhandler(404)
def not_found(error):
    print('error', error)
    return jsonify({'error': 'Not found'}), 404

@core_blueprint.route('/')
def core():
    return 'Flask Api'
