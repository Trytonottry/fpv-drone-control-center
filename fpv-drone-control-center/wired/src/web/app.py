from flask import Flask, render_template, request, jsonify
from src.autopilot.autopilot import Autopilot

app = Flask(__name__)
ap = Autopilot()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/arm", methods=["POST"])
def arm():
    ap.bridge.arm()
    return jsonify({"status": "armed"})

@app.route("/api/disarm", methods=["POST"])
def disarm():
    ap.bridge.disarm()
    return jsonify({"status": "disarmed"})

if __name__ == "__main__":
    ap.start()
    app.run(host="0.0.0.0", port=5000)