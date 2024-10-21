from sqlalchemy.orm import Session
from database import db
from sqlalchemy import select
from flask import jsonify
from models.productModels import Product
from middleware.productSchema import product_schema, products_schema

def add(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(
                name = product_data['name'],
                price = product_data['price'],
                description = product_data['description']
            )
            session.add(new_product)
            session.commit()
            return jsonify({
                    "status":"OK",
                    "message":"product added"
                }), 200
        
def edit(product_data):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product, product_data['id'])
            if not product:
                return jsonify({
                    "status":"BAD",
                    "message":"produt not found"
                }), 400
            product.name = product_data['name']
            product.description = product_data['description']
            product.price = product_data['price']
            session.commit()
            return jsonify({
                    "status":"OK",
                    "message":"product updated"
                }), 200

def remove(product_id):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product, product_id)
            if product:

                session.delete(product)
                session.commit()
                return jsonify({
                "status":"OK",
                "message":"product deleted"
                }), 200
            return jsonify({
                    "status":"BAD",
                    "message":"product not found"
                }), 200

def get_one(product_id):
    with Session(db.engine) as session:
        with session.begin():
            product = session.get(Product, product_id)
            if product:
                return product_schema.jsonify(product)
            return jsonify({
                    "status":"BAD",
                    "message":"product not found"
                }), 200
def get_all():
    with Session(db.engine) as session:
        with session.begin():
            products = session.query(Product).all()
            return products_schema.jsonify(products)