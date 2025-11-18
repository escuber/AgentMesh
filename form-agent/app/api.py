from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FormRequest(BaseModel):
    url: str
    step: str = "unknown"
    payload: dict = {}

@router.post("/process")
def process(req: FormRequest):
    return {
        "status": "received",
        "step": req.step,
        "url": req.url,
        "payload": req.payload
    }
