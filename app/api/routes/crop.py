from fastapi import APIRouter
from app.schemas.crop_schema import CropInput
from app.services.crop_service import recommend_crop

router = APIRouter(prefix="/crop", tags=["Crop Recommendation"])


@router.post("/recommend")
def crop_recommendation(data: CropInput):

    result = recommend_crop(data)

    return {"recommended_crop": result}
