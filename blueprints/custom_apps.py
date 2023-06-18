import os
from flask import Blueprint, request, render_template, redirect, url_for
from utils.response_utils import compose_response
from controllers.custom_app import CustomAppController

custom_app_blueprint = Blueprint("custom_app", __name__, url_prefix="/apps")

cac = CustomAppController()

@custom_app_blueprint.route("", methods=["GET", "POST"])
def get_apps():
    user_id = request.args.get("user_id", os.getenv("USER_ID"))
    print('user_id -> ', user_id)
    apps = cac.get_apps(user_id=user_id)
    if request.args.get("only_data"):
        return compose_response(apps)
    return render_template("apps.html", apps=apps)

@custom_app_blueprint.route("/configure", methods=["POST"])
def configure():
    app_id = request.json.get("id")
    app = cac.get_app_by_id(app_id)
    return compose_response(app)

@custom_app_blueprint.route("/user/create", methods=["POST"])
def create_user_app():
    user_id = os.getenv("USER_ID")
    data = request.json
    data["user_id"] = user_id
    cac.create_user_app(data)
    return redirect(url_for("custom_app.get_apps", user_id=user_id))
