import streamlit as st
from cat import classify_text

def run():
    name, confidence = classify_text(st.session_state.text)
    s_text = f'Category: {name}, Confidence: {confidence}'
    st.success(s_text)
    

st.set_page_config(
    page_title="NLP",
    layout="centered"
)


st.text_input("Enter Text to Categorize", key="text")
st.button("**RUN**", on_click=run())
