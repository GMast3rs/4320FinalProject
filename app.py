from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

def create_app():
    print("App is running")
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////app/databases/reservations.db"
    app.config["SECRET_KEY"] = "Secretkey"
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)


    from admin.routes import admin_bp
    app.register_blueprint(admin_bp)

    from reserve.routes import reserve_bp
    app.register_blueprint(reserve_bp)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
