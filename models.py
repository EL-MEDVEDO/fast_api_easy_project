from typing import Optional
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None