from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://root:czmpdrdv@localhost/advanced_e_commerce_api'
    DEBUG = True