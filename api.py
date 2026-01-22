from flask import Flask, jsonify, render_template
from monitoring import Monitoring
import threading,json,os

app = Flask(__name__)

# Path to JSON Lines log file
LOG_FILE = os.path.join("logs", "system_monitor.json")

# Create monitoring object
monitor = Monitoring()

# Start monitoring loop in background
monitor_thread = threading.Thread(
    target=monitor.monitoring_loop,
    daemon=True
)
monitor_thread.start()

@app.route("/")
def home():
    return jsonify({"status": "API running (JSON Lines mode)"})

# -------------------- ALL LOGS --------------------
@app.route("/logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"error": "Log file not found"}), 404

    logs = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                logs.append(json.loads(line))

    return jsonify(logs)

@app.route("/status")
def latest_status():
    # 🔥 LIVE DATA (NOT LOG FILE)
    return jsonify(monitor.live_data)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=True)

"""""
from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

LOG_FILE = os.path.join("logs", "system_monitor.json")

@app.route("/")
def home():
    return jsonify({"status": "API running (JSON Lines mode)"})

@app.route("/logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"error": "Log file not found"}), 404

    logs = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                logs.append(json.loads(line))

    return jsonify(logs)

@app.route("/status")
def latest_status():
    if not os.path.exists(LOG_FILE):
        return jsonify({"error": "Log file not found"}), 404

    last_logs = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                last_logs.append(json.loads(line))

    return jsonify(last_logs[-5:])

if __name__ == "__main__":
    app.run(debug=True)
"""""