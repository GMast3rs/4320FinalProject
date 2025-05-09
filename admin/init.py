from app import db


class Admin(db.Model):
    __tablename__ = 'admins'
    username = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
