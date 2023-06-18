import json
from time import sleep
from flask import Blueprint, request, render_template, redirect, url_for
from utils.response_utils import compose_response
from controllers.user_app import UserAppController

user_app_blueprint = Blueprint("user_app", __name__, url_prefix="/user_apps")

