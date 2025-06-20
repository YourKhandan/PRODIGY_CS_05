from app import create_app
from app.extensions import socketio
import os
app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7000))
    socketio.run(app, host="0.0.0.0", port=port, allow_unsafe_werkzeug=True)

