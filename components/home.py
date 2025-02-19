import streamlit as st

st.markdown("""
    <style>
            .block-container{
                margin:auto;
            }

            .text{
                text-align: center; 
                color: white;
            }

            .stButton{
                padding:auto;
                margin:auto;
            }
    </style>
""", unsafe_allow_html=True)


with st.container():
    st.markdown("""
                <h1 class='text'>Welcome to simple RAG system</h1>
                <p class='text'>This simple RAG system are built on top of AI generated data regarding the use of AI in digital marketing</p>
    """, unsafe_allow_html=True)