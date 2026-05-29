import numpy as np
import cv2

from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from fastapi import HTTPException

from app.models.dl_model import model

IMG_SIZE = 224

classes = [
    "Bacterial_spot",
    "Early_blight",
    "Late_blight",
    "Leaf_Mold",
    "Septoria_leaf_spot",
    "Spider_mites",
    "Target_Spot",
    "Yellow_Leaf_Curl_Virus",
    "Mosaic_virus",
    "Healthy",
]


def predict_disease(image_file):
    try:
        # Convert bytes → numpy array
        file_bytes = np.frombuffer(image_file.read(), np.uint8)

        # Decode image
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Could not decode image")

        # Convert BGR → RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

        # MobileNet preprocessing
        img = preprocess_input(img)

        # Add batch dimension
        img = np.expand_dims(img, axis=0)

        # Prediction
        prediction = model.predict(img, verbose=0)

        class_index = int(np.argmax(prediction))

        confidence = float(np.max(prediction))

        return {
            "disease": classes[class_index],
            "confidence": round(confidence * 100, 2),
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Disease prediction failed: {e}")
