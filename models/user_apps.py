from models.custom_apps import CustomApps

class UserApps(CustomApps):
    parent: str = None
    user_id: str = None
    disabled: bool = False
    
