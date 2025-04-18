from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_status_endpoint():
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert "cpu_percent" in data
    assert "memory_percent" in data

def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; version=0.0.4; charset=utf-8"
    content = response.text
    assert "system_cpu_usage_percent" in content
    assert "system_memory_usage_percent" in content
