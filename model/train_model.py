import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib

# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv("dataset/Crop_recommendation.csv")

print(data.head())

# ==========================================
# FEATURES & LABELS
# ==========================================

X = data.drop("label", axis=1)

y = data["label"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================
# MODEL
# ==========================================

model = RandomForestClassifier()

# ==========================================
# TRAINING
# ==========================================

model.fit(X_train, y_train)

# ==========================================
# PREDICTIONS
# ==========================================

predictions = model.predict(X_test)

# ==========================================
# ACCURACY
# ==========================================

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy}")

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(model, "models/crop_model.pkl")

print("Model Saved Successfully")
