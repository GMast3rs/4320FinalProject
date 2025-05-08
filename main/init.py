from flask import request, flash
from flask_sqlalchemy import SQLAlchemy
from models import Reservation  

def get_user_input():
    first_name = request.form.get('first_name', '').strip()
    last_name = request.form.get('last_name', '').strip()
    seat_row = request.form.get('seat_row', '').strip()
    seat_column = request.form.get('seat_column', '').strip()
    
    errors = []
    
    if not first_name:
        errors.append("First name is required.")
    if not last_name:
        errors.append("Last name is required.")
    if not seat_row or not seat_column:
        errors.append("Seat row and column are required.")
    else:
        try:
            seat_row = int(seat_row)
            seat_column = int(seat_column)
        except ValueError:
            errors.append("Seat row and column must be numbers.")

    # Seat must be available
    if not errors:  
        seat_taken = Reservation.query.filter_by(seat_row=seat_row, seat_column=seat_column).first()
        if seat_taken:
            errors.append(f"Seat {seat_row}-{seat_column} is already taken.")

    if errors:
        for error in errors:
            flash(error, 'error')  
        return {"errors": errors}  
    else:
        return {
            'first_name': first_name,
            'last_name': last_name,
            'seat_row': seat_row,
            'seat_column': seat_column
        }