import streamlit as st

st.markdown("""
    <style>
            .block-container{
                max-width:85%!important;
            }
    </style>
""", unsafe_allow_html=True)

if "loading" not in st.session_state:
    st.session_state["loading"] = False

def change_state():
    st.session_state["loading"] = True

def chat_actions(role:str, prompt:str):
    params = st.query_params
    if st.session_state["identifier"] not in st.session_state["chat_history"]:
        st.session_state["chat_history"][st.session_state["identifier"]] = []

    # Save user
    st.session_state["chat_history"][params["uuid"]].append({"role": "user", "content": prompt})
    
    # Init bot response
    text = st.session_state["chatbot"].interact(prompt)['result']
    st.session_state["chat_history"][params["uuid"]].append({"role": "assistant", "content": str(text)})

def chat_interface():
    with st.container():
        params = st.query_params

        messages = st.container(height=700, border=False)
        if prompt := st.chat_input(
            placeholder = "Your message",
            max_chars = None,
            disabled = st.session_state["loading"],
            on_submit = change_state
        ):
            with st.spinner('Processing...'):
                chat_actions(
                    role="assistant",
                    prompt=prompt
                )

            # Change State
            st.session_state["loading"] = False
            st.rerun()

        if st.session_state["chat_history"]:
            if st.session_state["chat_history"][params["uuid"]]:
                for i in st.session_state["chat_history"][params["uuid"]]:
                    messages.chat_message(i["role"]).write(f'{i["content"]}')