from app import db


class Admin(db.Model):
    __tablename__ = 'admin'
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)

