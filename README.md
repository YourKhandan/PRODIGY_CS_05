# PRODIGY_CS_05
# NetPacSniff - Real-Time Packet Sniffer 

NetPacSniff is a real-time packet sniffer tool built with:

-  **Python**
-  **Flask + Flask-SocketIO**
-  **HTML, CSS, JavaScript** (clean UI)
-  **Scapy** for packet sniffing


## 🚀 Features

- Real-time DNS packet capturing  
- Live display of captured traffic on a web interface  
- Clean and modern frontend  
- Lightweight & easy to run locally
## Inside __init__.py... you need to change the code at line  and insert your own secret key.. details are given at the __init__.py code
 What is SECRET_KEY in Flask?
 Flask uses SECRET_KEY to secure cookies, sessions, forms and tokens.
Without it, users could tamper with data stored on their browser and send it back.
It basically signs (encrypts) the session data so Flask can verify it's valid.

## ⚠ Important Notice

**This application requires administrative privileges to run.**

> Packet sniffing requires raw access to network interfaces which needs elevated permissions.

On **Windows**, always run your terminal as:  
**"Run as Administrator"**

On **Linux/macOS**, use `sudo` if needed.

## ❌ Why this project can't be deployed to Render (or most cloud platforms)

- **Scapy’s low-level packet capturing** directly interacts with hardware interfaces.
- Cloud platforms like Render, Heroku, etc., do not allow raw socket access.
- Therefore, this tool is designed to run only on your **local machine**.

## 🛠 Setup Instructions

1. Clone the repository:
git clone https://github.com/yourusername/netpacsniff.git
cd netpacsniff

2. Install Dependencies
pip install -r requirements.txt

3. Run the application (ensure you're using administrator privileges):
python run.py

4.🌐 Access
Once running, open your browser at
http://127.0.0.1:7000

You’ll see live DNS packets displayed on the web interface.


## 📊 Technologies Used
Python 3.x
Flask
Flask-SocketIO
Scapy
HTML5, CSS3, JavaScript


