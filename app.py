from flask import Flask, Response, request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, Histogram
import os
import time

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total HTTP Requests'['method','endpoint','http_status'])

REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency', ['endpoint'])

@app.before_request()
def start_timer():
    request.start_time=time.time()

@app.after_request()
def record_metrics(response):
    resp_time = time.time() - request.start_time

    REQUEST_LATENCY.labels(request.path).observe(resp_time)
    REQUEST_COUNT.labels(
        request.method,
        request.path,
        response.status_code
    ).inc()

    return response


@app.route("/")
def home():
    return "Hello DevOps - Running in Production"

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype = CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)