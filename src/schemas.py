from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    day: int = Field(ge=1, le=31)
    month: int = Field(ge=1, le=12)
    name: str = Field(min_length=1, max_length=50)
    year: Optional[int] = Field(default=None, ge=1, le=2100)
    description: Optional[str] = Field(default=None, min_length=1, max_length=100)
