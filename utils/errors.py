from enum import Enum

class Error(Enum):
    def __init__(self, error_code, error_message):
        super().__init__()
        self.error_code = error_code
        self.error_message = error_message



class CustomError(Error):
    UNKNOWN_ERROR = (100, "Something went wrong")
    UNAUTHORIZED = (401, "Unauthorized")
    INVALID_CREDENTIALS = (402,'Invalid Credentials')
    USER_NOT_FOUND = (404, "User not found")
    USERS_NOT_FOUND = (404, "Users not found")
    