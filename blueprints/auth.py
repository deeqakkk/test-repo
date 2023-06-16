from flask import request, Blueprint
from controllers.user import UserController
from utils.response_utils import compose_response

auth_blueprint = Blueprint('auth', __name__, url_prefix="/auth")
uc = UserController()


@auth_blueprint.route("/login", methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    response = uc.create_or_get_user(email, password)
    return compose_response(response)