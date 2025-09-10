from flask import Flask, jsonify, request
import random, time, logging
from prometheus_flask_exporter import PrometheusMetrics
from datetime import datetime

app = Flask(__name__)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Prometheus metrics
metrics = PrometheusMetrics(app)
metrics.info("app_info", "Flask Observability App", version="1.0.0")

# ---- Helper: Logging each request ----
@app.after_request
def after_request(response):
    log_data = {
        "path": request.path,
        "status": response.status_code,
        "timestamp": datetime.utcnow().isoformat(),
    }
    logger.info(f"Request Log: {log_data}")
    return response


# ---- Routes ----
@app.route("/")
def home():
    return "Welcome to the Flask Observability App!"

@app.route("/about")
def about():
    return "This is a simple Flask app for observability experiments."

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/error")
def error():
    if random.random() < 0.3:  # 30% error chance
        logger.error("Random error triggered!")
        return "Internal Server Error", 500
    return "All good!", 200

@app.route("/slow")
def slow():
    delay = random.randint(2, 5)
    logger.warning(f"Slow request, sleeping for {delay} seconds")
    time.sleep(delay)
    return f"Response delayed by {delay} seconds"

@app.route("/items")
def items():
    items_list = ["item1", "item2", "item3", "item4"]
    logger.info("Items endpoint called")
    return jsonify(items_list)


# ---- Traffic Generator ----
@app.route("/generate-traffic")
def generate_traffic():
    import threading
    from traffic import simulate_traffic
    threading.Thread(target=simulate_traffic, daemon=True).start()
    return "Traffic generation started!", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
