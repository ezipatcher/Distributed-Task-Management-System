from fastapi import APIRouter
from database import tasks

router = APIRouter()

@router.get("/tasks")
def get_tasks():
    return tasks
