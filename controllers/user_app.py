from bson import ObjectId
from models.form_field import FieldMeta, FormField
from models.custom_apps import AppInfo, CustomApp
from models.user_apps import UserApps
from utils.errors import CustomError


class UserAppController:
    def get_user_apps(self, user_id):
        apps = [app for app in UserApps.find({"user_id": user_id})]
        if not len(apps):
            return []
        response = []
        for app in apps:
            app = app.dict()
            app["id"] = str(app["id"])
            del app["_id"]
            response.append(app)
        return response
    
    def create_user_app(self, data):
        print(data)
        custom_app = CustomApp.find_one({"_id": ObjectId(data["app_id"])})
        if not custom_app:
            return CustomError.APP_NOT_FOUND
        del data["app_id"]
        custom_app = custom_app.dict()
        user_app = custom_app.copy()
        del user_app["id"]
        del user_app["_id"]
        user_app["parent"] = str(custom_app["id"])
        user_app["user_id"] = data["user_id"]
        
        for form_field in user_app["form_fields"]:
            if data.get(form_field["name"]):
                form_field["value"] = data.get(form_field["name"])        
        
        form_fields = []
        if len(user_app.get("form_fields")):
            for field in user_app["form_fields"]:
                if field.get("meta"):
                    field["meta"] = FieldMeta.parse_obj(field["meta"])
                field = FormField.parse_obj(field)
                form_fields.append(field)
        user_app["form_fields"] = form_fields
        user_app["app_info"] = AppInfo.parse_obj(user_app.get("app_info"))
        app = UserApps.parse_obj(user_app)
        app.create()
        return app.dict()