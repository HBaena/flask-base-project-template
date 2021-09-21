from typing import Any
from passlib.hash import sha256_crypt

def coors_handle(response) -> Any:
    """
    Prevent CORS problems after each `request
    :param response: Response of any request
    :return: The same request
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE, PATCH')
    return response

def encript_password(password: str) -> str:
    return sha256_crypt.hash(password)


def verify_password(hash_: str, password: str) -> bool:
    return sha256_crypt.verify(password, hash_)