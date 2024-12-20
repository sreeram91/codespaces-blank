import streamlit as st
import pandas as pd
from openpyxl import load_workbook

uploaded_file = st.file_uploader("Upload excel file", type={"xlsx", "csv"})

if uploaded_file:
    wb = load_workbook(uploaded_file, data_only=True)
    sheet = wb.active
    data = sheet.values
    columns = next(data)
    df = pd.DataFrame(data, columns=columns)
    if st.button("Upload"):
        st.write(df)

