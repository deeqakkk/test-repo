from flask import Blueprint, request, render_template
from utils.response_utils import compose_response
from controllers.custom_app import CustomAppController

custom_app_blueprint = Blueprint("custom_app", __name__, url_prefix="/apps")

cac = CustomAppController()

@custom_app_blueprint.route("/", methods=["GET"])
def get_apps():
    apps = cac.get_apps()
    if request.args.get("only_data"):
        return compose_response(apps)
    return render_template("apps.html", apps=apps)