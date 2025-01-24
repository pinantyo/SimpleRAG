import streamlit as st
from components.utils import init_state

st.markdown("""
    <style>
            .block-container{
                max-width:85%!important;
            }
    </style>
""", unsafe_allow_html=True)

def chat_actions(role:str="user", text:str=None):
    params = st.query_params
    if st.session_state["identifier"] not in st.session_state["chat_history"]:
        st.session_state["chat_history"][st.session_state["identifier"]] = []

    if role == "user":
        st.session_state["chat_history"][params["uuid"]].append({"role": "user", "content": st.session_state["chat_input"]})
    else:
        st.session_state["chat_history"][params["uuid"]].append({"role": "assistant", "content": text})

with st.container():
    params = st.query_params

    messages = st.container(height=700, border=False)
    if prompt := st.chat_input(
        placeholder = "Your message",
        max_chars = None,
        disabled = False,
        on_submit = chat_actions,
        key = "chat_input"
    ):
        chat_actions(
            role="assistant",
            text="Assistant's answer"
        )

    if st.session_state["chat_history"]:
        if st.session_state["chat_history"][params["uuid"]]:
            for i in st.session_state["chat_history"][params["uuid"]]:
                messages.chat_message(i["role"]).write(f'{i["content"]}')