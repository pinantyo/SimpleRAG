import streamlit as st
from components.utils import init_state, add_new_chat


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