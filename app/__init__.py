from flask import Flask
from .database import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///reservations.db"
    app.config["SECRET_KEY"] = "Secretkey"

    db.init_app(app)
    
    with app.app_context():
        from . import routes

    return app