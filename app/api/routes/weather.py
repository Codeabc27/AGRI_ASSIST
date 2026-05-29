from fastapi import APIRouter

from app.services.weather_service import get_weather

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get("/{city}")
def weather(city: str):

    data = get_weather(city)

    return data
