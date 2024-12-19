import streamlit as st;
import random
import pandas as pd


st.dataframe(
    {
     "sl.no": [random.randint(1, 10) for _ in range(3)],
     "Region": ["Mumbai", "Bangalore", "Chennai"],
     "Values": ["avg_value", "min_value", "max_value"],
     }, 
     use_container_width=True
)

emp_details= {
    "name": ["raju", "arun", "sanjay", "deepak"],
    "age": [21, 22, 23, 34],
    "city": ["mumbai", "bangalore", "andra pradesh", "delhi"] 
}

st.dataframe(emp_details, use_container_width=True)

df = pd.DataFrame(emp_details)
st.data_editor(df, use_container_width=True)


