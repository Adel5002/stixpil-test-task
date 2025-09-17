from typing import Sequence

from fastapi import HTTPException
from sqlmodel import Session, select

from db.models import TaskCreate, Task, TaskUpdate


def task_create(task_data: TaskCreate, session: Session) -> Task:
    task = Task(
        description=task_data.description
    )

    session.add(task)
    session.commit()
    session.refresh(task)

    return task

def task_update(task_data: TaskUpdate, task_id: int, session: Session) -> Task:
    task_to_update = session.get(Task, task_id)

    if not task_to_update:
        raise HTTPException(status_code=404, detail='Task does not exists!')

    update_data = task_data.model_dump(exclude_unset=True)
    task_to_update.sqlmodel_update(update_data)
    session.add(task_to_update)
    session.commit()
    session.refresh(task_to_update)

    return task_to_update

def task_delete(task_id: int, session: Session) -> dict[str, bool]:
    task = session.get(Task, task_id)

    if not task:
        raise HTTPException(status_code=404, detail='Task does not exists!')

    session.delete(task)
    session.commit()

    return {'status': True}

def tasks_get(session: Session) -> Sequence[Task]:
    tasks = session.scalars(select(Task)).all()

    return tasks
