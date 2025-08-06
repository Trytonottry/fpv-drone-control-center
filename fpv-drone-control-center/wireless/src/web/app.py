import asyncio, json, threading, websockets
from flask import Flask, render_template, request

app = Flask(__name__)
DRONE_IP = "192.168.4.1"  # IP RPi в режиме AP или адрес по Wi-Fi

@app.route("/")
def index():
    return render_template("index.html")

async def send_rc(channels):
    uri = f"ws://{DRONE_IP}:8765"
    async with websockets.connect(uri) as ws:
        await ws.send(json.dumps({"channels": channels}))

@app.route("/api/arm", methods=["POST"])
def arm():
    channels = [1800, 1500, 1500, 1500] + [1500]*12
    asyncio.run(send_rc(channels))
    return {"status": "armed"}

@app.route("/api/disarm", methods=["POST"])
def disarm():
    channels = [1000, 1500, 1500, 1500] + [1500]*12
    asyncio.run(send_rc(channels))
    return {"status": "disarmed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)