from pydantic import BaseModel, conlist
from typing import List, Dict


class CandidateResponse(BaseModel):
    candidate: conlist(Dict, min_items=1)


class CandidateFastAPIInput(BaseModel):
    position: str = "Python Developer"
    location: str = "Colombia,Bogotá"
    skills: List[str] = ['python', 'django', 'aws', 'web development', 'postgres']
    n_candidate: int = 5
    augmented_skills: bool = False
    english_level: List[int] = [0, 6]
    exp_year: List[int] = [0, 100]
    talent_exp_completed: bool = False
