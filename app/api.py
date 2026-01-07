from fastapi import APIRouter, HTTPException
from app.models import InputModel, OutputModel
from app.service import process_value

router = APIRouter()


@router.post("/process", response_model=OutputModel)
def process_endpoint(payload: InputModel):
    try:
        result = process_value(payload.value)
        return OutputModel(result=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
