import streamlit as st
from uuid import uuid4
from components.chatbox import RAGCreation
from components.chat_interface_ui import chat_interface

import os

def init_state():
    if "chatbot" not in st.session_state:
        st.session_state["chatbot"] = RAGCreation(chunk_size=500, chunk_overlap=50)
        st.session_state["chatbot"].rag_pipeline(documents=[
            os.path.join(os.getcwd(), 'data/PDF/AI_in_Digital_Marketing_A_Comprehensive_Guide.pdf'),
            os.path.join(os.getcwd(), 'data/PDF/Harnessing_AI_for_Marketing_Success.pdf')
        ])

    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = {}

    if "identifier" not in st.session_state:
        st.session_state["identifier"] = None

    if "pages" not in st.session_state:
        st.session_state["pages"] = []


def new_state():
    st.session_state["identifier"] = str(uuid4())
    st.session_state["chat_history"][st.session_state["identifier"]] = []

# Widgets shared by all the pages
def add_new_chat():
    new_state()
    init_state()

    st.session_state["pages"].append(
        st.Page(
            chat_interface, #"components/chat_interface_ui.py", 
            title="New message",
            url_path=f"/?uuid={st.session_state["identifier"]}"
        )
    )