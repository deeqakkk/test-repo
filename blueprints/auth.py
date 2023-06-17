from flask import request, Blueprint
from utils.response_utils import compose_response
from controllers.auth import AuthController

auth_blueprint = Blueprint('auth', __name__, url_prefix="/auth")
ac = AuthController()

@auth_blueprint.route("/login", methods=["POST"])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    response = ac.authenticate(email, password)
    return compose_response(response)