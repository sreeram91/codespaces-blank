import streamlit as st

emp_details= {
    "name": ["raju", "arun", "sanjay", "deepak"],
    "age": [21, 22, 23, 34],
    "city": ["mumbai", "bangalore", "andra pradesh", "delhi"] 
}

name_filter = st.text_input("Filter by name")

col1, col2 = st.columns([2, 2])

with col1:
    age_filter = st.text_input("Filter by age")

with col2:
    city_filter = st.text_input("Filter by city")

filtered_data= {
    "name": [],
    "age": [],
    "city": []
}

for i in range(len(emp_details["name"])):
    name = emp_details["name"][i]
    age = emp_details["age"][i]
    city = emp_details["city"][i]
    
    if(
        (name_filter.lower() in name.lower()) and
        (age_filter == "" or (age_filter.isdigit() and int(age_filter) == age)) and
        (city_filter == "All" or city_filter.lower() in city.lower())
    ):
        
        filtered_data["name"].append(name)
        filtered_data["age"].append(age)
        filtered_data["city"].append(city)


st.dataframe(filtered_data, use_container_width=True)