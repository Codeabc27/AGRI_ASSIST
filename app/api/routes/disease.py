from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.disease_service import predict_disease

router = APIRouter(prefix="/disease", tags=["Disease Detection"])


@router.post("/predict")
async def predict(file: UploadFile = File(...)):

    result = predict_disease(file.file)

    return result
