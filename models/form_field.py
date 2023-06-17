from enum import Enum
from mongodb_odm import Document
from dataclasses import dataclass

class FieldType(Enum):
    TEXT = "text"
    NUMBER = "number"
    PASSWORD = "password"
    EMAIL = "email"
    CHECKBOX = "checkbox"
    TEXTAREA = "textarea"
    SELECT = "select"


class FieldMeta(Document):
    max_length: int = 100
    min_length: int = 3

    def __init__(self, **data):
        super().__init__(**data)
        self.__dict__.pop("id", None)
        self.__dict__.pop("_id", None)

class FormField(Document):
    type: str = FieldType.TEXT
    label: str = None
    name: str = None
    placeholder: str = None
    helper_text: str = None
    icon: str = None
    required: bool = False
    meta: FieldMeta = FieldMeta()
    options: list[str] = []

    def __init__(self, **data):
        super().__init__(**data)
        self.__dict__.pop("id", None)
        self.__dict__.pop("_id", None)
