from flask import Flask
from database import db
from schema import ma
from flask_swagger_ui import get_swaggerui_blueprint
from models.productModels import Product
from models.orderModels import Order, order_products
from models.userModels import User
from routes.userBP import user_blueprint
from routes.productBP import product_blueprint
from routes.orderBP import order_blueprint




SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name':'advanced_e_commerce_api'
    }
)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(f'config.{config_name}')
    db.init_app(app)
    ma.init_app(app)
    blue_print_config(app)
    with app.app_context():
        db.create_all()
    return app

def blue_print_config(app):
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(product_blueprint,url_prefix='/product')
    app.register_blueprint(order_blueprint,url_prefix='/order')
    app.register_blueprint(swaggerui_blueprint,url_prefix=SWAGGER_URL)

app = create_app('DevelopmentConfig')

if __name__ == '__main__':
    app.run(debug=True)