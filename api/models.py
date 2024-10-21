from datetime import datetime as dt

from typing import List
from pydantic import BaseModel


class Response(BaseModel):
    score: int
    description: str

class Question(BaseModel):
    title: str
    responses: List[Response]

class Scores(BaseModel):
    name: str
    scores: List[int]