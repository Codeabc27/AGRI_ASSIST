import streamlit as st
import requests

st.title("🌦 Weather Dashboard")

city = st.text_input("Enter City", "Mumbai")

if st.button("Get Weather"):
    with st.spinner("Fetching weather data..."):
        try:
            response = requests.get(f"http://127.0.0.1:8000/weather/{city}", timeout=30)

            if response.status_code == 200:
                data = response.json()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("🌡 Temperature", f"{data['temperature']} °C")

                    st.metric("💧 Humidity", f"{data['humidity']}%")

                with col2:
                    st.metric("💨 Wind Speed", f"{data['wind_speed']} m/s")

                    st.metric("☁ Condition", data["weather"])

            else:
                st.error("Weather API failed")

        except Exception as e:
            st.error(f"Error: {str(e)}")
