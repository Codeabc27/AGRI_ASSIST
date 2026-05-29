import streamlit as st

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AgriAssist",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main {
        background-color: #f7faf7;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 18px;
        font-weight: bold;
        background-color: #2e7d32;
        color: white;
    }

    .stButton>button:hover {
        background-color: #1b5e20;
        color: white;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1b5e20;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: gray;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# HOME PAGE
# ==========================================

st.markdown('<p class="title">🌾 AgriAssist AI Platform</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">AI-powered smart farming assistant</p>', unsafe_allow_html=True
)

st.divider()

st.success("Use the sidebar to explore features")
