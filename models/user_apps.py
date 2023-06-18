from time import time
from mongodb_odm import Document
from models.custom_apps import AppInfo, CustomApp
from models.form_field import FormField

class UserApps(Document):
    name: str = None
    description: str = None
    category: str = None
    display_image: str = None
    images: list[str] = None
    form_fields: list[FormField] = []
    app_info: AppInfo = AppInfo()
    published: bool = False
    parent: str = None
    user_id: str = None
    disabled: bool = False
    created_at: float = time()
    updated_at: float = time()