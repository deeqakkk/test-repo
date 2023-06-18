from time import time
from mongodb_odm import Document
from models.form_field import FormField

class AppInfo(Document):
    developer: str = None
    date_published: float = time()
    date_updated: float = time()
    pricing: dict = None
    version: str = "1.0"

    def __init__(self, **data):
        super().__init__(**data)
        self.__dict__.pop("id", None)
        self.__dict__.pop("_id", None)



class CustomApp(Document):
    name: str = None
    description: str = None
    category: str = None
    display_image: str = None
    images: list[str] = None
    form_fields: list[FormField] = []
    app_info: AppInfo = AppInfo()
    published: bool = False
    created_at: float = time()
    updated_at: float = time()

