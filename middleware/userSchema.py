from schema import ma
from marshmallow import fields

class User(ma.Schema):
    id = fields.Integer(required=False)
    name = fields.String(required=True)
    roles = fields.List(fields.String(),required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta():
        fields = ('id','name','roles','username','password')

class UserLogin(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta():
        fields = ('username','password')

user_schema = User()
users_schema = User(many=True)
login_schema = UserLogin()