from services import userServices
from marshmallow import ValidationError
from flask import request, jsonify
from middleware.userSchema import user_schema, login_schema
from utils.util import token_required, role_required

def create():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400
    return userServices.create(user_data)

@token_required
def edit():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"status": "BAD", "messages": e.messages}), 400
    return userServices.edit(user_data)

@token_required
def remove(id):
    return userServices.remove(id)

@token_required
def get_one(id):
    return userServices.get_one(id)

@token_required
def get_all():
    return userServices.get_all()

def login():
    try:
        login_data = login_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages),400
    return userServices.login(login_data)

