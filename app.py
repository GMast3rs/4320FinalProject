from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    print("App is running")
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////app/databases/reservations.db"
    app.config["SECRET_KEY"] = "Secretkey"
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)


    from admin.routes import admin_bp
    app.register_blueprint(admin_bp)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
