import io
from PIL import Image
import streamlit as st
import requests

st.title("🍅 Disease Detection")

st.write("Upload a leaf image and the model will predict the disease.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        img_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(img_bytes))
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Disease"):
            with st.spinner("Sending image to backend..."):
                url = "http://127.0.0.1:8000/disease/predict"
                files = {
                    "file": (
                        uploaded_file.name,
                        io.BytesIO(img_bytes),
                        uploaded_file.type,
                    )
                }
                try:
                    response = requests.post(url, files=files, timeout=30)

                    if response.status_code == 200:
                        result = response.json()

                        disease = result.get("disease")
                        confidence = result.get("confidence", 0)

                        st.success("Analysis Complete")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.subheader("🌿 Disease")
                            st.write(disease)

                        with col2:
                            st.subheader("📊 Confidence")
                            try:
                                conf_val = float(confidence)
                            except Exception:
                                conf_val = 0.0
                            st.progress(min(max(conf_val / 100.0, 0.0), 1.0))
                            st.write(f"{conf_val}%")

                        treatments = {
                            "Late_blight": "Use copper-based fungicide and avoid excess moisture.",
                            "Early_blight": "Remove infected leaves and apply organic fungicide.",
                            "Leaf_Mold": "Improve air circulation and reduce humidity.",
                            "Healthy": "Plant is healthy. Maintain proper watering.",
                        }

                        recommendation = treatments.get(
                            disease, "Consult an agriculture expert."
                        )

                        st.subheader("💊 Treatment Recommendation")
                        st.info(recommendation)

                    else:
                        st.error(f"Backend Error: {response.status_code}")

                except requests.exceptions.ConnectionError:
                    st.error(
                        "Cannot connect to FastAPI backend. Make sure uvicorn server is running."
                    )

                except requests.exceptions.Timeout:
                    st.error("Request timeout. Model is taking too long.")

                except Exception as e:
                    st.error(f"Unexpected Error: {str(e)}")

    except Exception as e:
        st.error(f"Cannot process uploaded image: {e}")
