# app/__init__.py
from flask import Flask
from .extensions import socketio
from .sniffer import start_sniffing
import threading

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7318b0edb5524f7eebb5ee11ea08c82a'

    from .routes import main
    app.register_blueprint(main)

    socketio.init_app(app)

    # Start sniffer thread after app is created
    sniffer_thread = threading.Thread(target=start_sniffing)
    sniffer_thread.daemon = True
    sniffer_thread.start()

    return app
