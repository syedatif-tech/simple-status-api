from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "name": "Simple Status API",
        "message": "API is running"
    })

@app.get("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.get("/status")
def status():
    return jsonify({
        "status": "operational",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
