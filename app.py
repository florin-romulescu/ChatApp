from flask import Flask
from flask_socketio import SocketIO, emit
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.register_blueprint(views)
socket = SocketIO(app)

@socket.on("connection")
def handle_connection(msg):
    print(msg)

@socket.on('message')
def handle_message(data):
    print("Received data:", data)
    emit("message-handler", data, broadcast=True)

if __name__ == '__main__':
    from database import *
    create_db()
    print(f"Database was created succsefully. Located at {PATH}.")
    
    socket.run(app)