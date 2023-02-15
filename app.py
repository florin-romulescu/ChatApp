from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views)

if __name__ == '__main__':
    from database import *
    create_db()
    print(f"Database was created succsefully. Located at {PATH}.")
    
    app.run(debug=True, port=8000)