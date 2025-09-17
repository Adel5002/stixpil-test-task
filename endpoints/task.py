from typing import Sequence

from fastapi import APIRouter

from db.crud import tasks_get, task_create, task_update, task_delete
from db.db import SessionDep
from db.models import Task, TaskRead, TaskCreate, TaskUpdate

router = APIRouter()

@router.get("/get-all", response_model=Sequence[TaskRead])
def get_tasks(session: SessionDep) -> Sequence[Task]:
    return tasks_get(session)


@router.post("/create", response_model=TaskRead, status_code=201)
def create_task(task_data: TaskCreate, session: SessionDep) -> Task:
    return task_create(task_data, session)


@router.patch("/update/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_data: TaskUpdate, session: SessionDep) -> Task:
    return task_update(task_data, task_id, session)


@router.delete("/delete/{task_id}", response_model=dict)
def delete_task(task_id: int, session: SessionDep) -> dict:
    return task_delete(task_id, session)