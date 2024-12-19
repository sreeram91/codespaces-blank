import streamlit as st;

col1, col2 = st.columns([3, 3])

with col1:
    user_input_region = st.text_input('Region', placeholder="Enter the Region");
    user_input_date = st.text_input('Start Date', placeholder='DD-MM-YYY');

with col2:
    user_input_time = st.text_input('Start Time', placeholder='HH:MM:SS');
    user_input_value = st.selectbox(
        'Selected Value',
        ['avg_value', 'max_value', 'min_value']
    )

if st.button("Execute"):
        region = user_input_region
        date = user_input_date
        time = user_input_time
        selected_value = user_input_value

        st.subheader("Data:")
        st.write(f"**Region**: {region}")
        st.write(f"**Start Date**: {date}")
        st.write(f"**Start Time**: {time}")
        st.write(f"**Selected Value**: {selected_value}")




