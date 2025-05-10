from flask import Blueprint, request, render_template, redirect, flash, url_for
from admin.init import Admin
from admin.models import Reservation, db
from app import get_cost_matrix

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        admin = Admin.query.filter_by(username=username).first()

        if admin and admin.password == password:
            return redirect('/admin/dashboard')
        else:
            return render_template('admin.html', message="Login failed")

    return render_template('admin.html', message="Please login")

@admin_bp.route('/admin/dashboard', methods=['GET'])
def dashboard():
    reservations = Reservation.query.all()
    
    pricing = get_cost_matrix()
    total_sales = sum(pricing[r.seatRow][r.seatColumn] for r in reservations)
    
    return render_template(
        'adminloggedin.html',
        reservations=reservations,
        total_sales=total_sales,
        pricing=pricing
    )

@admin_bp.route('/admin/delete/<int:reservation_id>', methods=['POST'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    
    db.session.delete(reservation)
    db.session.commit()
    
    flash('Reservation deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))
