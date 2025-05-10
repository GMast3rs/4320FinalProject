from flask import Blueprint, render_template, request, redirect, url_for, flash
from reserve.init import get_user_input
from admin.models import Reservation
from app import db

reserve_bp = Blueprint('reserve', __name__)

@reserve_bp.route('/reserve', methods=['GET', 'POST'])
def reservation():
    reservations = Reservation.query.all()
    
    if request.method == 'POST':
        reservation_data = get_user_input()
        if reservation_data:
            new_res = Reservation(
                passengerName=f"{reservation_data['first_name']} {reservation_data['last_name']}",
                seatRow=reservation_data['seat_row'],
                seatColumn=reservation_data['seat_column'],
                eTicketNumber=reservation_data['e_ticket'],

            )
            db.session.add(new_res)
            db.session.commit()
            flash("Seat Reserved Successfully")
            return redirect(url_for('reserve.reservation'))
    
    return render_template('reserve.html', reservations=reservations)
