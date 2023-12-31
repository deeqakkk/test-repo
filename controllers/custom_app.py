import json
from bson import ObjectId
from dataclasses import asdict
from models.custom_apps import AppInfo, CustomApp
from models.form_field import FieldMeta, FormField
from utils.errors import CustomError
from controllers.user_app import UserAppController

uac  = UserAppController()

class CustomAppController:
    def create_apps(self, data_list):
        for data in data_list:
            form_fields = []
            if len(data.get("form_fields")):
                for field in data["form_fields"]:
                    if field.get("meta"):
                        field["meta"] = FieldMeta.parse_obj(field["meta"])
                    field = FormField.parse_obj(field)
                    form_fields.append(field)
            data["form_fields"] = form_fields
            data["app_info"] = AppInfo.parse_obj(data.get("app_info"))
            app = CustomApp.parse_obj(data)
            app.create()
        return True

    def get_apps(self, user_id):
        apps = CustomApp.find()
        response = []
        for app in apps:
            app = app.dict()
            app["id"] = str(app["id"])
            del app["_id"]
            response.append(app)
        user_apps = []
        if user_id is not None:
            user_apps = uac.get_user_apps(user_id)
        
        return {"apps": response, "my_apps": user_apps}
    
    def get_app_by_id(self, app_id: str):
        app = CustomApp.find_one({"_id": ObjectId(app_id)})
        if not app:
            return CustomError.APP_NOT_FOUND
        app.id = str(app.id)
        app._id = str(app._id)
        return app.dict()
    
    def create_user_app(self, data):
        response = uac.create_user_app(data)
        return response

