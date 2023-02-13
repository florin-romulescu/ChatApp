from flask import Blueprint
from flask import render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return "Test"

@views.route("/auth")
def auth():
    return render_template("auth.html")