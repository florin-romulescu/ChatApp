from flask import Flask
from flask import redirect, render_template
from flask import url_for

app = Flask(__name__)

@app.route("/")
def init():
    return redirect("/index")

@app.route("/index")
def index():
    return render_template("index.html")