from typing import Optional

from sqlmodel import SQLModel, Field


class Task(SQLModel, table=True):
    id: int = Field(primary_key=True)
    description: str

class TaskCreate(SQLModel):
    description: str

class TaskUpdate(SQLModel):
    description: Optional[str] = None

class TaskRead(SQLModel):
    id: int
    description: str