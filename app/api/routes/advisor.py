from fastapi import APIRouter

from app.services.farming_advisor import generate_farming_advice

router = APIRouter(prefix="/advisor", tags=["AI Farming Advisor"])


@router.get("/{city}")
def farming_advisor(city: str):

    result = generate_farming_advice(city)

    return result
