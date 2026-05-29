import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ==========================================
# GET WEATHER
# ==========================================


def get_weather(city):

    from fastapi import HTTPException

    if not API_KEY:
        raise HTTPException(status_code=500, detail="Weather API key not configured")

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=data.get("message", "Weather API Error"),
            )

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
        }

    except HTTPException:
        raise
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Weather API request failed: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get weather: {e}")
