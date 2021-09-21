from flask import Flask  # Core of flask apps 
from flask_restful import Api  # modules for fast creation of apis
from os import path, getcwd
from DB import PosgresConnection  # DB connection
from flask_jwt_extended import JWTManager  # JWT authorization
from datetime import timedelta  # Needed for expiration token time


def connect_to_db_from_json(filename: str):
    return PosgresConnection(path.join(getcwd(), filename))


app = Flask(__name__)  # Creating flask app
app.secret_key = ''  # Declaring secret api

api = Api(app)  # Creating API object from flask app

# keys for JWT auth
app.config['JWT_SECRET_KEY'] = ''
app.config['JWT_PUBLIC_KEY'] = ''
app.config['JWT_PRIVATE_KEY'] = ''
# Expiration time for JWT tokens
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=7)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
# Needed for customs responses on JWT exceptions
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["DEBUG"] = False

jwt = JWTManager(app) # Creating JWT auth manager 