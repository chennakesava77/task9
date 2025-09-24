from fastapi import FastAPI

app = FastAPI(title="Task Service")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "task-service"}


# Example endpoint (task creation placeholder)
@app.post("/tasks")
def create_task(title: str, description: str = ""):
    return {"message": "Task created successfully", "title": title, "description": description}
