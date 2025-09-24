from fastapi import FastAPI
import httpx

app = FastAPI(title="Gateway Service")

USER_SERVICE_URL = "http://user-service:8000"
TASK_SERVICE_URL = "http://task-service:8001"


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "gateway-service"}


@app.get("/users/health")
async def user_health():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{USER_SERVICE_URL}/health")
        return r.json()


@app.get("/tasks/health")
async def task_health():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{TASK_SERVICE_URL}/health")
        return r.json()
