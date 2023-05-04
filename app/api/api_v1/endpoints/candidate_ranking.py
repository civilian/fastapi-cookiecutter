import os
from app.utils.aiservices import AIInterface
from fastapi import Depends, HTTPException, status, APIRouter
from json.decoder import JSONDecodeError
from starlette.responses import JSONResponse

from app.api.deps import get_current_user
from app.crud import create_feedback
from app.schemas.candidate import CandidateRankingInput, CandidateResponse
from app.schemas.feedback import FeedbackInput

router = APIRouter()


@router.post("/find-candidate/", tags=["Candidates Ranking"], dependencies=[Depends(get_current_user)])
async def calculate_candidates_ranking(data: CandidateRankingInput) -> CandidateResponse:
    ai_interface = AIInterface(
        "FASTAPI",
        job_name=data.position,
        job_site=data.location,
        job_skills=data.skills,
        top_n=data.n_candidate,
        augmented_skills=data.augmented_skills,
        min_max_exp_years=data.exp_year,
        min_max_english=data.english_level,
        talent_experience_only=data.talent_exp_completed,
    )
    try:
        response = ai_interface.make_request()
        return response
    except JSONDecodeError as e:
        HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )


@router.post("/feedback/", tags=["Candidates Ranking Feedback"], dependencies=[Depends(get_current_user)])
async def save_candidates_ranking_feedback(data: FeedbackInput) -> dict:
    create_feedback(data)

    return JSONResponse(
        {"message": "Feedback successfully processed"},
        status_code=status.HTTP_201_CREATED,
    )
