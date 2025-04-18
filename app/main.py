from fastapi import FastAPI
import psutil
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Prometheus metrics
cpu_gauge = Gauge("system_cpu_usage_percent", "CPU usage percent")
mem_gauge = Gauge("system_memory_usage_percent", "Memory usage percent")

@app.get("/status")
def get_status():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    return {"cpu_percent": cpu, "memory_percent": memory}

@app.get("/metrics")
def metrics():
    cpu_gauge.set(psutil.cpu_percent())
    mem_gauge.set(psutil.virtual_memory().percent)
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
