import streamlit as st

# Employee details
emp_details = {
    "name": ["raju", "arun", "sanjay", "deepak"],
    "age": [21, 22, 23, 34],
    "city": ["mumbai", "bangalore", "andra pradesh", "delhi"]
}

# Filter by name
name_filter = st.text_input("Filter by Name (type a name):")

# Filter by city
city_filter = st.selectbox(
    "Filter by City:", 
    options=["All"] + list(set(emp_details["city"]))  # Add "All" option
)

# Filter by age range
min_age, max_age = st.slider(
    "Filter by Age Range:", 
    min_value=0, 
    max_value=100, 
    value=(0, 100)
)

# Apply filters
filtered_data = {
    "name": [],
    "age": [],
    "city": []
}

for i in range(len(emp_details["name"])):
    name = emp_details["name"][i]
    age = emp_details["age"][i]
    city = emp_details["city"][i]

    if (
        (name_filter.lower() in name.lower()) and
        (city_filter == "All" or city_filter == city) and
        (min_age <= age <= max_age)
    ):
        filtered_data["name"].append(name)
        filtered_data["age"].append(age)
        filtered_data["city"].append(city)

# Display filtered results
st.dataframe(filtered_data, use_container_width=True)
