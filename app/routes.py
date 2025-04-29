from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database import db
from app.models import Reservation, Admin

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/admin", methods=["GET", "POST"])
def admin_login():

@main_bp.route("/reserve", methods=["GET", "POST"])
def reserve_seat():

def get_cost_matrix():
    return [[100, 75, 50, 100] for _ in range(12)]