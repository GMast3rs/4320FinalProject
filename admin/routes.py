from flask import Blueprint, request, render_template
from admin.init import Admin

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        admin = Admin.query.filter_by(username=username).first()

        if admin and admin.password == password:
            return render_template('adminloggedin.html')
        else:
            return render_template('admin.html', message="Login failed")

    return render_template('admin.html', message="Please login")
