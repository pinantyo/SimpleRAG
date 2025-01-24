import streamlit as st
from uuid import uuid4

def init_state():
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = {}

    if "identifier" not in st.session_state:
        st.session_state["identifier"] = None

    if "pages" not in st.session_state:
        st.session_state["pages"] = [] # st.Page("components/chat_interface_ui.py", title="chat1")


def new_state():
    st.session_state["identifier"] = str(uuid4())
    st.session_state["chat_history"][st.session_state["identifier"]] = []