from sqlalchemy.orm import Session
from models.orderModels import Order
from models.productModels import Product
from database import db
from flask import jsonify
from middleware.orderSchema import order_schema, orders_schema
from sqlalchemy import select

def get_products(product_ids):
    with Session(db.engine) as session:
        with session.begin():
            return session.execute(select(Product).where(Product.id.in_(product_ids))).scalars().all()


def place(order_data):
    with Session(db.engine) as session:
        with session.begin():
            new_order = Order(
                user_id=order_data['user_id'],
                products=get_products(order_data['products'])
            )
            session.add(new_order)
            session.commit()
            return jsonify({
                    "status":"OK",
                    "message":"order added"
                }), 200
        
def edit(order_data):
    with Session(db.engine) as session:
        with session.begin():
            order = session.get(Order, order_data['id'])
            if order:
                order.user_id = order_data['user_id']
                order.products=get_products(order_data['products'])
                session.commit()
                return jsonify({
                    "status":"OK",
                    "message":"order updated"
                }), 200
            return jsonify({
                    "status":"BAD",
                    "message":"order not found"
                }), 400
        
def remove(order_id):
    with Session(db.engine) as session:
        with session.begin():
            order = session.get(Order, order_id)
            if order:
                session.delete(order)
                session.commit()
                return jsonify({
                    "status":"OK",
                    "message":"order removed"
                }), 200
            else:
                return jsonify({
                    "status":"BAD",
                    "message":"order not found"
                }), 400

def get_one(order_id):
    with Session(db.engine) as session:
        with session.begin():
            order = session.get(Order, order_id)
            if order:
                return order_schema.jsonify(order)

def get_all():
    with Session(db.engine) as session:
        with session.begin():
            orders = session.query(Order).all()
            return orders_schema.jsonify(orders)