from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

def send_notifications():
    count = 1
    while True:
        time.sleep(5)
        socketio.emit('notification', {
            'message': f'New Notification #{count}'
        })
        count += 1

if __name__ == '__main__':
    thread = threading.Thread(target=send_notifications)
    thread.daemon = True
    thread.start()

    socketio.run(app, debug=True)