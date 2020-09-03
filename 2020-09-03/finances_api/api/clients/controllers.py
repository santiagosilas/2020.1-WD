from flask import Flask, jsonify, request, abort 
from api.clients.models import Client
from api.clients.services import ClientService
from api.clients.schemas import ClientSchema
from api import db, ma

from . import clients_blueprint as blueprint

@blueprint.errorhandler(404)
def not_found(error):
    print('error', error)
    return jsonify({'error': 'Not found'}), 404

@blueprint.route('/api/clients', methods=['GET'])
def get_clients():
    clients = ClientService.get_all()
    clients_schema = ClientSchema(many=True)
    return clients_schema.jsonify(clients)

@blueprint.route('/api/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = ClientService.get_by_id(client_id)
    if client == None:
        abort(404)
    client_schema = ClientSchema()
    return client_schema.jsonify(client)    

@blueprint.route('/api/clients', methods=['POST'])
def create_client():
    username = request.json['username']
    email = request.json['email']
    
    if ClientService.get_by_username(username):
        return jsonify({'error': 'This username already exists!'})

    if ClientService.get_by_email(email):
        return jsonify({'error': 'This email already exists!'})

    client = ClientService.add(username, email)
    
    client_schema = ClientSchema()
    return client_schema.jsonify(client)

@blueprint.route('/api/clients/<int:client_id>', methods=['PUT'])
def update_user(client_id):

    username = request.json['username']
    email = request.json['email']    

    if ClientService.get_by_username(username):
        return jsonify({'error': 'This username already exists!'})

    if ClientService.get_by_email(email):
        return jsonify({'error': 'This email already exists!'})

    client = ClientService.update(
        client_id, username, email)

    if client == None:
        abort(404)

    client_schema = ClientSchema()
    return client_schema.jsonify(client)

@blueprint.route('/api/clients/<int:client_id>', methods=['PATCH'])
def update_partial_client(client_id):
    username = request.json['username']

    if ClientService.get_by_username(username):
        return jsonify({'error': 'This username already exists!'})

    client = ClientService.update_username(
        client_id, username)

    if client == None:
        abort(404)

    client_schema = ClientSchema()
    return client_schema.jsonify(client)


@blueprint.route('/api/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = ClientService.remove(client_id)

    if client == None:
        abort(404)

    client_schema = ClientSchema()
    return client_schema.jsonify(client)