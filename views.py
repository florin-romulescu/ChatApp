from flask import Blueprint
from flask import render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/auth")
def auth():
    return render_template("auth.html")

@views.route("/register")
def register():
    return render_template("register.html")

@views.route("/about")
def about():
    return render_template("about.html")