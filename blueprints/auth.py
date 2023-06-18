from flask import request, Blueprint, redirect
from utils.errors import CustomError
from utils.response_utils import compose_response
from controllers.auth import AuthController

auth_blueprint = Blueprint('auth', __name__, url_prefix="/auth")
ac = AuthController()

@auth_blueprint.route("/login", methods=["POST"])
def login():
    if not request.form:
        request.form = request.json
    email = request.form.get('email')
    password = request.form.get('password')
    response = ac.authenticate(email, password)
    if isinstance(response, CustomError):
        return compose_response(response)
    return redirect(location="/apps")
