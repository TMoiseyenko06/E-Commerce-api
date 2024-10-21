from services import orderServices
from marshmallow import ValidationError
from flask import request, jsonify
from middleware.orderSchema import order_schema
from utils.util import token_required, role_required

@token_required
@role_required("customer")
def place():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    return orderServices.place(order_data)

@token_required
@role_required("employee")
def edit():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    return orderServices.edit(order_data)

@token_required
@role_required("admin")
def remove(id):
    return orderServices.remove(id)

@token_required
@role_required("customer")
def get_one(id):
    return orderServices.get_one(id)


@token_required
@role_required("customer")
def get_all():
    return orderServices.get_all()

