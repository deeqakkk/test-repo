from mongodb_odm import ASCENDING, Document, IndexModel


class User(Document):
    username: str = None
    email: str = None
    password: str = None

    class Config(Document.Config):
        indexes = [
            IndexModel([("username", ASCENDING)]),
        ]