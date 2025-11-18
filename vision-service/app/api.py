from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VisionRequest(BaseModel):
    payload: str

@router.post("/process")
def process(req: VisionRequest):
    return {"status": "received", "echo": req.payload}
