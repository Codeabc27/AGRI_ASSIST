````markdown
# 🌾 AgriAssist
---

# 🚜 Overview

AgriAssist is an AI-powered smart farming assistant platform that helps farmers and agriculture enthusiasts make data-driven decisions using Artificial Intelligence, Machine Learning, and Retrieval-Augmented Generation (RAG).

The platform combines:

- 🌿 Plant Disease Detection
- 🤖 AI Agriculture Chatbot
- 🌦 Weather Monitoring
- 🌾 Crop Recommendation System

Built using FastAPI, Streamlit, TensorFlow, LangChain, ChromaDB, and Groq LLM.

---

# ✨ Features

## 🌿 Plant Disease Detection

- Tomato leaf disease classification
- CNN + MobileNetV2 model
- Image upload support
- Confidence score prediction
- Treatment recommendations

---

## 🤖 AI Agriculture Chatbot

- RAG-based agriculture assistant
- LangChain + ChromaDB integration
- Groq LLM support
- Context-aware farming guidance

---

## 🌦 Weather Dashboard

- Real-time weather monitoring
- Temperature tracking
- Humidity analysis
- Wind speed insights
- Farming weather recommendations

---

## 🌾 Crop Recommendation

Predicts suitable crops using:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall

---

# 🧰 Tech Stack

| Category | Technologies |
|---|---|
| Language | Python |
| Backend | FastAPI, Uvicorn |
| Frontend | Streamlit |
| Deep Learning | TensorFlow, MobileNetV2 |
| Machine Learning | Scikit-learn |
| Computer Vision | OpenCV |
| RAG Pipeline | LangChain, ChromaDB |
| LLM | Groq API |
| Data Processing | Pandas, NumPy |

---

# 🏗️ System Architecture

```text
Streamlit Frontend
       │
       ▼
FastAPI Backend
├── Disease Detection API
├── Crop Recommendation API
├── Weather API
├── RAG Chatbot API
       │
       ▼
AI/ML Services
├── CNN + MobileNetV2
├── Crop ML Model
├── ChromaDB Vector Store
└── Groq LLM
````

---

# 📁 Project Structure

```text
AGRI_ASSIST/
│
├── app/
│   ├── api/routes/
│   ├── services/
│   ├── models/
│   └── core/
│
├── frontend/
│   ├── app.py
│   └── pages/
│
├── frontend/assets/
│
├── model/
│   ├── train_cnn.py
│   ├── train_model.py
│   └── mobilenet_tomato_model.h5
│
├── RAG/
│   ├── ingest.py
│   ├── rag_pipeline.py
│   └── data/
│
├── dataset/
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Codeabc27/AGRI_ASSIST.git

cd AGRI_ASSIST
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
WEATHER_API_KEY=your_openweather_api_key

GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Application

## Start FastAPI Backend

```bash
uvicorn app.main:app --reload
```

---

## Start Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

# 🧠 Model Training

## Train Disease Detection Model

```bash
python model/train_cnn.py
```

---

## Train Crop Recommendation Model

```bash
python model/train_model.py
```

---

# 🔗 API Endpoints

| Endpoint           | Method | Description            |
| ------------------ | ------ | ---------------------- |
| `/`                | GET    | Health Check           |
| `/disease/predict` | POST   | Disease Detection      |
| `/crop/recommend`  | POST   | Crop Recommendation    |
| `/weather/{city}`  | GET    | Weather Information    |
| `/rag/ask`         | POST   | AI Agriculture Chatbot |

---

# 📊 Model Performance

| Model                    | Accuracy |
| ------------------------ | -------- |
| Tomato Disease Detection | 94%      |
| Crop Recommendation      | 98%      |

---

# 📸 Screenshots

Store screenshots inside:

```text
frontend/assets/
```

### Suggested Screenshots

| Feature             | File Name                            |
| ------------------- | ------------------------------------ |
| Disease Detection   | `screenshot-disease-detection.png`   |
| AI Chatbot          | `screenshot-chatbot.png`             |
| Weather Dashboard   | `screenshot-weather-dashboard.png`   |
| Crop Recommendation | `screenshot-crop-recommendation.png` |
| Agri AI Chat        | `screenshot-agri-ai-chat.png`        |

---

# 🛣 Future Improvements

* Multi-crop disease detection
* Voice assistant integration
* IoT sensor integration
* Mobile application
* Docker deployment
* Authentication system

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to GitHub
5. Open Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by Codeabc27

GitHub:
https://github.com/Codeabc27

---

# 🙏 Acknowledgements

* Kaggle Tomato Disease Dataset
* FastAPI
* Streamlit
* TensorFlow
* LangChain
* ChromaDB
* Groq

```
```

