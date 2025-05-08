from flask import Blueprint, request
from app import db

admin_bp = Blueprint('admin', __name__)


class Admin(db.Model):
    __tablename__ = 'admin'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

@admin_bp.route('/login', methods=['POST'])
def login():
    admin_details = request.get_json()
    username = admin_details.get('username')
    password = admin_details.get('password')

    admin = Admin.query.filter_by(username = username)
    if admin and admin.password == password:
        return "Admin login sucessfull"
    else:
        "Admin login failed"

