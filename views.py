from flask import Blueprint
from flask import render_template, request
from database import insert_user, get_user

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/login", methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        user_name = request.form["username"]
        password = request.form["password"]

        user_data = get_user(user_name, password)
        if user_data == None:
            return render_template("auth.html", err=True)

        return render_template("index.html", user=user_data[1])
    
    return render_template("auth.html")

@views.route("/register", methods=['POST', 'GET'])
def register():
    err = False
    if request.method == 'POST':
        user_name = request.form["username"]
        password = request.form["password"]

        err = insert_user(user_name, password, False)
    
    return render_template("register.html", err=err)

@views.route("/about")
def about():
    return render_template("about.html")