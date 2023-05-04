from datetime import datetime

from app.db.connector import db
from app.models.feedback import FeedbackCR, FeedbackQuestionCR
from app.schemas import feedback


def create_feedback(feedback: feedback.FeedbackInput):
    data = feedback.dict()
    data.update({
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    })

    questions = data.pop("questions", [])

    with db.atomic():
        db_feedback = FeedbackCR.create(**data)

        for question in questions:
            question.update({
                "feedback_fastapi_id": db_feedback.id
            })

        FeedbackQuestionCR.insert_many(questions).execute()
