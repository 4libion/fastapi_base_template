from typing import Optional

from pydantic import BaseModel, ConfigDict


class SchemeTaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class SchemeTask(SchemeTaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SchemeTaskId(BaseModel):
    ok: bool = True
    task_id: int