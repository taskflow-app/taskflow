from fastapi import APIRouter
from models.task import Task

router = APIRouter()

tasks = []

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task 