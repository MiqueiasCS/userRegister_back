from flask import Flask
from flask_migrate import Migrate

def init_app(app:Flask):
    from app.models.user_model import UserModel
    from app.models.address_model import AddressModel

    Migrate(app,app.db)