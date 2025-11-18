from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class JobAnalysisRequest(BaseModel):
    resume: str
    job_description: str

@router.post("/process")
def process(req: JobAnalysisRequest):
    return {
        "status": "received",
        "summary": "placeholder",
        "resume_length": len(req.resume),
        "jd_length": len(req.job_description)
    }
