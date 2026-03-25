from flask import Flask
from prometheus_client import Counter, generate_latest
import os

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total HTTP Requests')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello DevOps - Running in Production"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/metrics")
def metrics():
    return generate_latest, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
