import os
import jwt
from flask import request
from functools import wraps
from utils.response_utils import compose_response
from utils.errors import CustomError

secret_key = os.getenv("SECRET_KEY")


def login_required(func):
    @wraps(func)
    def decorator(*agrs, **kwargs):
        token = request.headers.get("Authorization")
        user_id = None
        if not token:
            return compose_response(CustomError.UNAUTHORIZED)
        try:
            token = token.split(" ")[-1]
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            user_id = payload["user_id"]
        except jwt.ExpiredSignatureError:
                return compose_response(CustomError.UNAUTHORIZED)
        except jwt.InvalidTokenError:
            return compose_response(CustomError.UNAUTHORIZED)
        return func(user_id)
    return decorator
