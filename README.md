---

# 🖥️ System Resource Monitor API

A lightweight FastAPI-based service to monitor system resources like CPU, memory, and disk usage. The API exposes real-time system metrics and integrates with Prometheus and Grafana for observability. Built with Docker, deployed via GitHub Actions.

---

## 🚀 Features

- `/status` endpoint for JSON-formatted system stats
- `/metrics` endpoint for Prometheus scraping
- CI/CD pipeline via GitHub Actions
- Dockerized app with Prometheus & Grafana stack

---

## 📌 Tech Stack

- **Backend**: Python 3.12, FastAPI
- **Monitoring**: Prometheus + Grafana
- **CI/CD**: GitHub Actions
- **Containerization**: Docker + Docker Compose

---

## 📂 Endpoints

### `GET /status`

Returns JSON response with:
- CPU usage (%)
- Memory usage (%)
- Disk usage (%)

### `GET /metrics`

Exposes metrics in Prometheus-compatible format for automatic scraping.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/system-monitor-api
cd system-monitor-api
```

### 2. Run Locally (without Docker)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Run with Docker Compose

```bash
docker-compose up --build
```

- Prometheus: [http://localhost:9090](http://localhost:9090)
- Grafana: [http://localhost:3000](http://localhost:3000) (Default login: `admin` / `admin`)

### 4. Add GitHub Secrets

In your GitHub repo:
- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

---

## ⚙️ CI/CD Pipeline

### Trigger:
- Runs on every `push` to `main`

### Steps:
1. Checkout code
2. Install dependencies & run unit tests
3. Build Docker image
4. Log in to Docker Hub (via GitHub Secrets)
5. Push image to Docker Hub

---

## 📚 Learnings

- FastAPI-based REST API development
- Prometheus metrics integration
- Grafana dashboard creation
- Dockerization of microservices
- CI/CD automation with GitHub Actions

---

## 📄 License

MIT License

The MIT License (MIT)

Copyright (c) 2011-2025 The Bootstrap Authors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 🙌 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)

---

Feel free to fork, star ⭐, or contribute!

---

