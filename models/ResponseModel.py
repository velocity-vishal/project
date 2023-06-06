from typing import TypeVar
from pydantic import BaseModel

T = TypeVar("T")

class ResponseModel(BaseModel):
    message: str
    status: int
    data: T

