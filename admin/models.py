from app import db

class Reservation(db.Model):
    __tablename__ = 'reservations'
    
    id = db.Column(db.Integer, primary_key=True)
    passengerName = db.Column(db.String)
    seatRow = db.Column(db.Integer)
    seatColumn = db.Column(db.Integer)
    eTicketNumber = db.Column(db.String)
    created = db.Column(db.DateTime)
