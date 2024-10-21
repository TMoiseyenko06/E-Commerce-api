from flask import Blueprint
from controllers import orderControllers

order_blueprint = Blueprint('order_blueprint',__name__)
order_blueprint.route('',methods=['POST'])(orderControllers.place)
order_blueprint.route('',methods=['PUT'])(orderControllers.edit)
order_blueprint.route('<int:id>',methods=['DELETE'])(orderControllers.remove)
order_blueprint.route('<int:id>',methods=['GET'])(orderControllers.get_one)
order_blueprint.route('',methods=['GET'])(orderControllers.get_all)