import streamlit as st
from uuid import uuid4

def init_state():
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if "identifier" not in st.session_state:
        st.session_state["identifier"] = str(uuid4())