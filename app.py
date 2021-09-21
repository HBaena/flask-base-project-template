from flask import request  # Flask, receiving data from requests, json handling
from flask import jsonify  # Flask, receiving data from requests, json handling
# from flask import send_file  # Create url from statics files
# from flask import send_from_directory  # Create url from statics files
from flask_restful import Resource  # modules for fast creation of apis

from werkzeug.exceptions import HTTPException

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import get_jwt
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import verify_jwt_in_request

from config import app  # Importing main app
from config import api  # Importing api builder
from config import jwt  # Importing JWT manager
from config import connect_to_db_from_json  # Function to connect to db from a json config file

# from model.user import User  # The way to import models
# from controller.user import User  # The way to import controllers
from model.enum import StatusMsg, ErrorMsg, AuthError

from functions import coors_handle, encript_password, verify_password

from functools import wraps

from os import path, getcwd

from typing import Any, NoReturn

from icecream import ic  # module for debuging

@app.after_request
def after_request(response) -> Any:
    return coors_handle(response)


@app.before_first_request
def initialize() -> NoReturn:
    ic("INIT")
    # Initialization
    ...
    # Path(path.join(getcwd(), "temp")).mkdir(parents=True, exist_ok=True)  # For example, Create a folder 
    # global db_connection
    # db_connection = connect_to_db_from_json(path.join(getcwd(), "db_credentals.json"))

@jwt.expired_token_loader
def my_expired_token_callback(jwt_header, jwt_payload):
    return jsonify(status="token_expired", error=ErrorMsg.AUTH_ERROR, log=jwt_payload, message=AuthError.EXPIRED_TOKEN), 401


@jwt.invalid_token_loader
def my_invalid_token_callback(jwt_payload):
    return jsonify(status="invalid_token", error=ErrorMsg.AUTH_ERROR, log=jwt_payload, message=AuthError.INVALID_TOKEN), 401


@jwt.unauthorized_loader
def my_unauthorized_callback(jwt_payload):
    return jsonify(status="unauthorized", error=ErrorMsg.AUTH_ERROR, log=jwt_payload, message=AuthError.UNAUTHORIZED), 401


def jwt_required_in_db():
    """
    Function: jwt_required_in_db
    Summary: Custom jwt validation
    """
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            token = request.headers['Authorization'][7:]  # bearer: ...
            # if user_model.validate_token(token):  # Validate 
            #     return fn(*args, **kwargs)
            # else:
                # return jsonify(status="invalid_token", error="Token is not in db")
            return jsonify(status=StatusMsg.OK)
        return decorator
    return wrapper

class Test(Resource):
    """
        DECLARING A CLASS FOR EACH RESTFULL ENDPOINT
    """

    def get(self):
        # parameters = request.args
        return jsonify(status=StatusMsg.OK, method='get')

    def post(self):
        # form_data = request.form
        # files_data = request.files
        return jsonify(status=StatusMsg.OK, method='post')

    def delete(self):
        return jsonify(status=StatusMsg.OK, method='delete')

    def put(self):
        return jsonify(status=StatusMsg.OK, method='put')

    def patch(self):
        return jsonify(status=StatusMsg.OK, method='patch')


class Login(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        # CHECK credentials
        # user_hash = user_model.get_hash(username)
        # if not verify_password(user_hash, password):
        #     return jsonify(status=StatusMsg.OK, error=ErrorMsg.WRONG_PASSWORD, ), 401

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        # user_model.jwt(access_token)  # Write token int db
        response = jsonify(dict(
            estatus="good", 
            message="Verified", 
            data=dict(
                username=username,
                access_token=access_token,
                refresh_token= refresh_token)
                )
            )
        set_access_cookies(response, access_token)
        return response


api.add_resource(Test, '/', '/test/')
api.add_resource(Login, '/login/')


@app.errorhandler(Exception)
def handle_exception(e):
    ic(e)
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return jsonify(status=StatusMsg.FAIL, log=str(e), error='http_exception'), 400

    # now you're handling non-HTTP exceptions only
    return jsonify(status=StatusMsg.FAIL, log=str(e), error='internal_server_error'), 500
