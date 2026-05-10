"""Модуль с классом Task"""

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str = Field(max_length=50)
    priority: int = Field(ge=1, le=5)
    status: bool = False
