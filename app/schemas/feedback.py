from pydantic import BaseModel, conlist, constr, conint
from typing import Any

from .utils import PeeweeGetterDict


class FeedbackQuestion(BaseModel):
    question: constr(max_length=300)
    score: conint(ge=1, le=5)

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class FeedbackInput(BaseModel):
    endpoint: constr(max_length=500)
    text_feedback: constr(max_length=154)
    questions: conlist(FeedbackQuestion, min_items=1)

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
