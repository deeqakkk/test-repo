from models.user import User
from utils.errors import CustomError
from utils.util import encrypt_password

class UserController:
    def create_or_get_user(self, email, password):
        cipher_password = encrypt_password(password)
        user = User.find_one({"email": email})
        if user and user.password != cipher_password:
            return CustomError.INVALID_CREDENTIALS
        if not user:
            user = User(
                email=email,
                password=cipher_password,
                username=email
            )
            user.create()
            
        user.password = None
        return user.__dict__
        

    