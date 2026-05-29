import os

from dotenv import load_dotenv

from groq import Groq

from app.services.weather_service import get_weather

load_dotenv()

# ==========================================
# GROQ CLIENT
# ==========================================

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ==========================================
# AI FARMING ADVICE
# ==========================================


def generate_farming_advice(city):

    # ======================================
    # GET WEATHER
    # ======================================

    from fastapi import HTTPException

    weather = get_weather(city)

    if not isinstance(weather, dict) or weather.get("error"):
        raise HTTPException(
            status_code=502, detail="Failed to retrieve weather for advisor"
        )

    # ======================================
    # EXTRACT WEATHER DATA
    # ======================================

    try:
        temperature = weather["temperature"]
        humidity = weather["humidity"]
        condition = weather["weather"]
        wind_speed = weather["wind_speed"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Invalid weather data: {e}")

    # ======================================
    # PROMPT
    # ======================================

    prompt = f"""

You are AgriAssist AI.

Provide smart farming advice based on current weather.

Weather Details:

City: {city}

Temperature: {temperature} °C

Humidity: {humidity} %

Condition: {condition}

Wind Speed: {wind_speed} m/s

Give:
- disease risk
- irrigation advice
- farming precautions
- crop care recommendations

Keep response practical and farmer-friendly.
"""

    # ======================================
    # GROQ RESPONSE
    # ======================================

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )

        answer = response.choices[0].message.content

        return {"weather": weather, "advice": answer}

    except Exception as e:
        raise HTTPException(status_code=502, detail=f"AI advisor request failed: {e}")
