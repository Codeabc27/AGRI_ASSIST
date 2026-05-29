import streamlit as st
import requests

# ==========================================
# PAGE TITLE
# ==========================================

st.title("🤖 AgriAssist AI Chat")

st.write("Ask agriculture-related questions")

# ==========================================
# CHAT HISTORY
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# USER INPUT
# ==========================================

prompt = st.chat_input("Ask your farming question...")

# ==========================================
# PROCESS QUESTION
# ==========================================

if prompt:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # ======================================
    # AI RESPONSE
    # ======================================

    with st.chat_message("assistant"):
        with st.spinner("AgriAssist Thinking..."):
            response = requests.post(
                "http://127.0.0.1:8000/rag/ask", json={"question": prompt}
            )

            if response.status_code == 200:
                result = response.json()

                answer = result["answer"]

            else:
                answer = "API Error"

            st.markdown(answer)

    # Store assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})
