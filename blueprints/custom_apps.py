import json
from flask import Blueprint, request, render_template, redirect, url_for
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

@custom_app_blueprint.route("/configure", methods=["POST"])
def configure():
    app_id = request.json.get("id")
    app = cac.get_app_by_id(app_id)
    return compose_response(app)
    

# @custom_app_blueprint.route("/form")
# def form_element():
#     data = json.loads(request.args['data'])
#     print(data)
#     return render_template("form.html", data=data)
    