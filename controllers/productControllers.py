from services import productServices
from marshmallow import ValidationError
from flask import jsonify,request
from middleware.productSchema import product_schema, products_schema
from utils.util import token_required, role_required

@token_required
@role_required("employee")
def add():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    return productServices.add(product_data)

@token_required
@role_required("employee")
def edit():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages)
    return productServices.edit(product_data)

@token_required
@role_required("admin")
def remove(id):
    return productServices.remove(id)

@token_required
@role_required("customer")
def get_one(id):
    return productServices.get_one(id)

@token_required
@role_required("customer")
def get_all():
    return productServices.get_all()

