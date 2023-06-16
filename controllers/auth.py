import os
import jwt
from controllers.user import UserController
from utils.errors import CustomError

uc = UserController()
secret_key = os.getenv("SECRET_KEY")

class AuthController:
    def authenticate(self, email, password):
        response = uc.create_or_get_user(email, password)
        if isinstance(response, CustomError):
            return response
        token = jwt.encode({
            "user_id": str(response["id"]),
            "email": response["email"]
            }, secret_key, algorithm="HS256")
        return token
    
    