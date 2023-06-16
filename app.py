from dotenv import load_dotenv
load_dotenv() 

import os
import yaml
import json
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    print(os.getenv("PORT"))
    return "Server is up and running"

def register_blueprints(swagger_blueprint):
    app.register_blueprint(swagger_blueprint)

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

@app.route('/docs')
def swagger():
    with open('./api-docs.yaml') as f:
        return json.dumps(yaml.safe_load(f))


if __name__ == "__main__":
    swagger_blueprint = add_swagger_ui()
    register_blueprints(swagger_blueprint)
    app.run(host="0.0.0.0", port=os.getenv("PORT"), debug=True)