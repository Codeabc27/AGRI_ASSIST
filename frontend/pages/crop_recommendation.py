import streamlit as st
import requests

st.title("🌾 Crop Recommendation")

st.write("Enter soil and climate values")

# ==========================================
# INPUTS
# ==========================================

nitrogen = st.number_input("Nitrogen")

phosphorus = st.number_input("Phosphorus")

potassium = st.number_input("Potassium")

temperature = st.number_input("Temperature")

humidity = st.number_input("Humidity")

ph = st.number_input("pH")

rainfall = st.number_input("Rainfall")

# ==========================================
# BUTTON
# ==========================================

if st.button("Recommend Crop"):
    payload = {
        "nitrogen": nitrogen,
        "phosphorus": phosphorus,
        "potassium": potassium,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall,
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/crop/recommend", json=payload, timeout=30
        )

        if response.status_code == 200:
            result = response.json()
            st.success("Recommendation Complete")
            st.subheader("🌾 Recommended Crop")
            st.write(result.get("recommended_crop"))
        else:
            # Try to extract backend message
            try:
                err = response.json().get("error")
            except Exception:
                err = None
            st.error(err or f"API Error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to backend. Ensure the FastAPI server is running.")
    except requests.exceptions.Timeout:
        st.error("Request timed out. Try again later.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")
