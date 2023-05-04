from playhouse.reflection import generate_models

from app.db.connector import db, models

FeedbackCR = models.get("fastapi_feedbackcr")
FeedbackQuestionCR = models.get("fastapi_feedbackquestioncr")
