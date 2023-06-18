import os
import json
from time import sleep
from flask import Blueprint, request, render_template, redirect, url_for
from utils.response_utils import compose_response
from controllers.user_app import UserAppController

user_app_blueprint = Blueprint("user_app", __name__, url_prefix="/user_apps")
uac = UserAppController()

@user_app_blueprint.route("", methods=["GET"])
def get_user_app():
    app_id = request.args.get("app_id")
    user_id = request.args.get("user_id", os.getenv("USER_ID"))
    return compose_response(uac.get_app_by_id(app_id, user_id))