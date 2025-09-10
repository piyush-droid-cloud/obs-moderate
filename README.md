# 🚀 Flask Observability Project with Prometheus, Grafana, Loki & Blackbox

This project demonstrates **modern observability practices** using a simple Flask web application monitored with the **PGMLB stack**:
- **Prometheus** – Collect metrics
- **Grafana** – Visualize metrics & logs
- **Loki + Promtail** – Centralized logging
- **Blackbox Exporter** – External probing
- **Docker Compose** – Orchestration

---

## 📌 Features
- Flask app with endpoints:
  - `/health` → Health check
  - `/error` → Simulated errors
  - `/slow` → Simulated latency
  - `/metrics` → Prometheus metrics
- Auto traffic generator to simulate load
- Logs (INFO, WARNING, ERROR) shipped to Loki
- Prometheus scrapes metrics from Flask & Blackbox
- Grafana dashboards with:
  - Request rate
  - Error rate
  - Latency monitoring
  - Uptime probes
  - Logs correlated with metrics

---

## 🛠️ Tech Stack
- Python (Flask)
- Docker & Docker Compose
- Prometheus
- Grafana
- Loki + Promtail
- Blackbox Exporter

---

## ⚡ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/flask-observability.git
cd flask-observability
2. Start the stack
bash
Copy code
docker-compose up --build
3. Access services
Flask App → http://localhost:5000

Prometheus → http://localhost:9090

Grafana → http://localhost:3000 (default: admin/admin)

Loki → http://localhost:3100

📊 Grafana Dashboard



🔮 Next Steps
Add database + cache services

Create alerting rules in Prometheus

Deploy on Kubernetes

🙌 Contributing
PRs are welcome! Suggestions & improvements are always appreciated.
