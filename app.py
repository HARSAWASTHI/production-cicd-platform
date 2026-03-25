from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
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
    return Response(generate_latest(), mimetype = CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)