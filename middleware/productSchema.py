from schema import ma
from marshmallow import fields

class Product(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta():
        fields = ('id','name','description','price')

product_schema = Product()
products_schema = Product(many=True)