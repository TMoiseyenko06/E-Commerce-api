from flask import Blueprint
from controllers import userControllers

user_blueprint = Blueprint('user_blueprint',__name__)
user_blueprint.route('',methods=['POST'])(userControllers.create)
user_blueprint.route('',methods=['PUT'])(userControllers.edit)
user_blueprint.route('/<int:id>',methods=['DELETE'])(userControllers.remove)
user_blueprint.route('/<int:id>',methods=['GET'])(userControllers.get_one)
user_blueprint.route('',methods=['GET'])(userControllers.get_all)