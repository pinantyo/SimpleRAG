import streamlit as st
from components.utils import init_state

# Widgets shared by all the pages
with st.sidebar:
    if st.button(
        "Start new message",
        icon=None,
        use_container_width=True,
        type='secondary'
    ):
        init_state()

pg = st.navigation(
    {
        "Prompts" : [
            st.Page("components/chat_interface_ui.py", title="chat1"), 
            st.Page("components/chat_interface_ui.py", title="chat2", url_path="chat2")
        ]
    },
    position='sidebar',
    expanded=False
)
pg.run()