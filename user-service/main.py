from fastapi import FastAPI

app = FastAPI(title="User Service")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "user-service"}


# Example endpoint (user registration placeholder)
@app.post("/users/register")
def register_user(username: str, password: str):
    return {"message": f"User '{username}' registered successfully"}
