# app.py

import streamlit as st

# Title of the web page
st.title('Welcome to My Sample Website!')

# Add a header
st.header('This is a header')

# Add a subheader
st.subheader('This is a subheader')

# Add some text
st.write('Hello, this is a sample text on the website.')

# Add an image
st.image('https://via.placeholder.com/150', caption='Sample Image')

# Add a button
if st.button('Click Me'):
    st.write('Button was clicked!')

# Add a text input
user_input = st.text_input('Enter your name:')
if user_input:
    st.write(f'Hello, {user_input}!')

# Add a selectbox
option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {option}')

# Add a checkbox
if st.checkbox('Check me'):
    st.write('Checkbox is checked!')

# Add a slider
slider_value = st.slider('Select a value:', 0, 100, 50)
st.write(f'Slider value: {slider_value}')