from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Notification Service Running"}

@app.get("/notifications")
def get_notifications():
    return {
        "notifications": [
            "Task Assigned",
            "Task Completed"
        ]
    }
