from flask import Flask, jsonify, request, abort 
from api.models.user import User, UserSchema
from api import app, db, ma

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_schema = UserSchema(many=True)
    return users_schema.jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user == None:
        abort(404)
    
    user_schema = UserSchema()
    return user_schema.jsonify(user)    

@app.route('/api/users', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    user = User(username, email)

    db.session.add(user)
    db.session.commit()

    user_schema = UserSchema()
    return user_schema.jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user == None:
        abort(404)

    username = request.json['username']
    email = request.json['email']    

    user.username = username
    user.email = email

    db.session.commit()

    user_schema = UserSchema()
    return user_schema.jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user == None:
        abort(404)
    
    db.session.delete(user)
    db.session.commit()

    user_schema = UserSchema()
    return user_schema.jsonify(user)   