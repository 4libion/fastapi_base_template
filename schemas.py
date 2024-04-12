from typing import Optional

from pydantic import BaseModel


class SchemeTaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class SchemeTask(SchemeTaskAdd):
    id: int


class SchemeTaskId(BaseModel):
    ok: bool = True
    task_id: int