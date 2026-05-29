import numpy as np
from fastapi import HTTPException

from app.models.ml_model import model


def recommend_crop(data):
    try:
        features = np.array(
            [
                [
                    data.nitrogen,
                    data.phosphorus,
                    data.potassium,
                    data.temperature,
                    data.humidity,
                    data.ph,
                    data.rainfall,
                ]
            ]
        )

        prediction = model.predict(features)

        return prediction[0]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Crop recommendation failed: {e}")
