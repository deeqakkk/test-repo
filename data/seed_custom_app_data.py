import json
from controllers.custom_app import CustomAppController

cac = CustomAppController()

def seed_custom_app_data():
    with open("data/seed_data.json", 'r') as f:
        data = json.load(f)
        cac.create_apps(data)
        


