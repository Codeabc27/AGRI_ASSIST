import streamlit as st
import requests

st.title("🤖 AI Farming Advisor")

st.write("Get weather-aware farming advice")

city = st.text_input("Enter City", "Chennai")

if st.button("Generate Advice"):
    with st.spinner("Generating AI Advice..."):
        try:
            response = requests.get(f"http://127.0.0.1:8000/advisor/{city}", timeout=60)

            if response.status_code == 200:
                data = response.json()

                weather = data.get("weather")

                advice = data.get("advice")

                # ==================================
                # WEATHER
                # ==================================

                st.subheader("🌦 Current Weather")

                if weather:
                    st.write(f"🌡 Temperature: {weather.get('temperature')} °C")
                    st.write(f"💧 Humidity: {weather.get('humidity')} %")
                    st.write(f"☁ Condition: {weather.get('weather')}")
                else:
                    st.write("Weather data unavailable")

                # ==================================
                # AI ADVICE
                # ==================================

                st.subheader("🤖 AI Farming Advice")
                if advice:
                    st.success(advice)
                else:
                    st.info("No advice returned from AI service.")

            else:
                try:
                    err = response.json().get("error")
                except Exception:
                    err = None
                st.error(err or f"API Error: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Ensure the FastAPI server is running.")
        except requests.exceptions.Timeout:
            st.error("Request timed out. The AI may be slow — try again later.")
        except Exception as e:
            st.error(f"Unexpected error: {e}")
