from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from database import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/reservations.db"
    app.config["SECRET_KEY"] = "Secretkey"

    db.init_app(app)

    from admin.init import admin_bp
    app.register_blueprint(admin_bp)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
