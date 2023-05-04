import os
from fastapi import FastAPI, Depends, HTTPException, status
from json.decoder import JSONDecodeError
from starlette.responses import JSONResponse

from app.api.api_v1.api import api_router
from app.api.deps import get_current_user
from app.core.config import settings
from app.crud import create_feedback
from app.db.connector import db_state_default, db
from app.schemas.candidate import CandidateRankingInput, CandidateResponse
from app.schemas.feedback import FeedbackInput

app = FastAPI(name="Fast Api Microservice")

app.include_router(api_router, prefix=settings.API_V1_STR)
