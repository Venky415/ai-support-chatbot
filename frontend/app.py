import streamlit as st
import requests

# ==============================
# Backend API URL
# ==============================
API_URL = "http://127.0.0.1:8000/chat"

# ==============================
# Page Config
# ==============================
st.set_page_config(
    page_title="AI Support Chatbot",
    page_icon="💬",
    layout="centered"
)

st.title("💬 AI Support Chatbot")

# ==============================
# Initialize Chat History
# ==============================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==============================
# Display Previous Messages
# ==============================
for role, message in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

# ==============================
# User Input Box (ChatGPT Style)
# ==============================
user_query = st.chat_input("Ask a question...")

# ==============================
# When User Sends Message
# ==============================
if user_query:

    # 1️⃣ Store user message
    st.session_state.messages.append(("user", user_query))

    # 2️⃣ Show user message instantly
    st.chat_message("user").write(user_query)

    try:
        # 3️⃣ Send request to backend
        response = requests.post(
            API_URL,
            json={"question": user_query}
        )

        # 4️⃣ Handle success
        if response.status_code == 200:
            answer = response.json()["answer"]

        else:
            answer = "⚠️ Backend error. Please try again."

    except Exception as e:
        answer = "❌ Error connecting to backend."

    # 5️⃣ Store bot response
    st.session_state.messages.append(("assistant", answer))

    # 6️⃣ Display bot response
    st.chat_message("assistant").write(answer)
