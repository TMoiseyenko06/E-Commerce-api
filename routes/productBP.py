from flask import Blueprint
from controllers import productControllers

product_blueprint = Blueprint('product_blueprint',__name__)
product_blueprint.route('',methods=['POST'])(productControllers.add)
product_blueprint.route('',methods=['PUT'])(productControllers.edit)
product_blueprint.route('/<int:id>',methods=['DELETE'])(productControllers.remove)
product_blueprint.route('/<int:id>',methods=['GET'])(productControllers.get_one)
product_blueprint.route('',methods=['GET'])(productControllers.get_all)