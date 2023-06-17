from flask import Blueprint
from utils.login_utils import login_required

user_blueprint = Blueprint('user', __name__, url_prefix="/user")

@user_blueprint.route("/", methods=["GET"])
@login_required
def get_user(user_id: str):
    return "true"
    
