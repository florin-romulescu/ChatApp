from flask import Flask

@app.route("/")
def init():
    return "<h1>ChatApp</h1>"

if __name__ == '__main__':
    app = Flask(__name__)