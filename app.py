from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/reservations.db"
    app.config["SECRET_KEY"] = "Secretkey"

    db.init_app(app)

    from .admin import admin_bp
    app.register_blueprint(admin_bp)

    return app
