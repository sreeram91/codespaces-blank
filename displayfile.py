import streamlit as st
import pandas as pd

# File uploader
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])

if uploaded_file:
    df = pd.read_text(uploaded_file)
    if st.button("Upload"):
        st.write(df)