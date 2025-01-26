import streamlit as st
from uuid import uuid4
from components.chatbox import ChatBot, RAGCreation
import os

def init_state():
    if "chatbot" not in st.session_state:
        st.session_state["chatbot"] = RAGCreation(chunk_size=500, chunk_overlap=50)
        st.session_state["chatbot"].rag_pipeline(documents=[
            os.path.join(os.getcwd(), 'src', 'data/PDF/AI_in_Digital_Marketing_A_Comprehensive_Guide.pdf'),
            os.path.join(os.getcwd(), 'src', 'data/PDF/Harnessing_AI_for_Marketing_Success.pdf')
        ])

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = {}

    if "identifier" not in st.session_state:
        st.session_state["identifier"] = None

    if "pages" not in st.session_state:
        st.session_state["pages"] = [] # st.Page("components/chat_interface_ui.py", title="chat1")


def new_state():
    st.session_state["identifier"] = str(uuid4())
    st.session_state["chat_history"][st.session_state["identifier"]] = []