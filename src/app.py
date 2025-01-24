import streamlit as st
from components.utils import init_state, new_state

# Widgets shared by all the pages
def add_new_chat():
    new_state()

    st.session_state["pages"].append(
        st.Page(
            "components/chat_interface_ui.py", 
            title="chat1",
            url_path=f"/?uuid={st.session_state["identifier"]}"
        )
    )



init_state()

with st.sidebar:
    st.button(
        "Start new message",
        icon=None,
        use_container_width=True,
        type='secondary',
        on_click=add_new_chat
    )

pg = st.navigation(
    {
        "Menu" : [st.Page("components/home.py", title="Home", url_path="/")],
        "Prompts" : st.session_state["pages"]
    },
    position='sidebar',
    expanded=False
)
pg.run()