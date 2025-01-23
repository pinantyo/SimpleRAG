import streamlit as st


st.markdown("""
    <style>
            .block-container{
                max-width:85%!important;
            }
    </style>
""", unsafe_allow_html=True)

def page1():
    st.write(st.session_state.foo)

def page2():
    st.write(st.session_state.bar)

# Widgets shared by all the pages
with st.sidebar:
    st.button(
        "Start new message",
        on_click = None,
        icon = None,
        disabled=False,
        use_container_width=True,
        type='secondary'
    )


    st.navigation(
        [st.Page(page1, title="Hi"), st.Page(page2, title="Hi2")],
        position='sidebar',
        expanded=False
    )

with st.container():
    messages = st.container(height=700, border=False)
    if prompt := st.chat_input(
        placeholder = "Your message",
        max_chars = None,
        disabled = False,
        on_submit = None,
    ):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")



    