from schema import ma
from marshmallow import fields

class Order(ma.Schema):
    id = fields.Integer(required=False)
    user_id = fields.Integer(required=True)
    products = fields.List(fields.Integer(),required=True)

    class Meta():
        fields = ("id","user_id","products")

order_schema = Order()
orders_schema = Order(many=True)