from dotenv import load_dotenv
load_dotenv() 

import os
import yaml
import json
from flask import Flask, request, render_template
from flask_swagger_ui import get_swaggerui_blueprint
from config.db_manager import DBManager
from blueprints import *
from data.seed_custom_app_data import seed_custom_app_data

app = Flask(__name__)


def register_blueprints(swagger_blueprint):
    blueprints = [
        swagger_blueprint, auth_blueprint, 
        user_blueprint, custom_app_blueprint
        ]
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

def add_swagger_ui():
    SWAGGER_URL = "/api-docs"
    API_URL = "/docs"

    return get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            "app_name": "Swagger UI"
        }
    )

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/test', methods=["GET"])
def index():
    return "Server is up and running"

@app.route('/docs')
def swagger():
    with open('./api-docs.yaml') as f:
        return json.dumps(yaml.safe_load(f))

if __name__ == "__main__":
    try:
        DBManager.initialize_instance()
    except:
        print("Unable to initialize DB")
        exit(0)

    swagger_blueprint = add_swagger_ui()
    register_blueprints(swagger_blueprint)
    # seed_custom_app_data()
    app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=True)