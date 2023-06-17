import os
from mongodb_odm import connect


class DBManager:
    _db = None

    def __init__(self):
        DBManager._db = connect(os.getenv("MONGO_URL"))


    @staticmethod
    def initialize_instance():
        return DBManager()

    @staticmethod
    def get_db():
        return DBManager._db