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
    if role == "user":
        st.session_state["chat_history"].append(
            {"id":st.session_state["identifier"], "role": "user", "content": st.session_state["chat_input"]},
        )
    else:
        st.session_state["chat_history"].append(
            {"id":st.session_state["identifier"], "role": "assistant", "content": text},
        )

init_state()
with st.container():
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
        for i in st.session_state["chat_history"]:
            messages.chat_message(i["role"]).write(f'{i["id"]} - {i["content"]}')