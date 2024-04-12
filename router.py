from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import SchemeTask, SchemeTaskAdd, SchemeTaskId


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks",],
)


@router.post("")
async def add_task(
    task: Annotated[SchemeTaskAdd, Depends()],
) -> SchemeTaskId:
    task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[SchemeTask]:
    tasks = await TaskRepository.get_tasks()
    return tasks