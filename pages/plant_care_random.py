import streamlit as st

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Plant Care - Random")
st.write("This is the screen for Plant Care with the Random option.")
st.write("Here, you can add specific content or functionality for this option.")

# Custom CSS for button styling
st.markdown("""
    <style>
    .stButton > button {
        width: 150px;  /* Button width */
        height: 50px;  /* Button height */
        margin: 10px auto;  /* Center buttons within their columns */
        display: block;  /* Ensure centering works */
        transition: all 0.3s ease;  /* Smooth transition for hover effect */
        border: 2px solid #000000;  /* Default border */
    }
    /* Normal state */
    .stButton > button {
        color: #000000;  /* Default text color */
        background-color: #ffffff;  /* Default background */
    }
    /* Hover state */
    .stButton > button:hover {
        color: #3b6945;  /* Text color on hover */
        background-color: #f0f0f0;  /* Background color on hover */
        border-color: #3b6945;  /* Border color on hover */
    }
    img {
        margin-left: 50px;
    }
    div.stButton > button > div > p {
        font-size: 24px !important;  /* Adjust size */
    }
    </style>
""", unsafe_allow_html=True)

# Add option buttons
st.write("Choose an option:")
option_col1, option_col2 = st.columns(2)
with option_col1:
    if st.button("My Plants"):
        st.switch_page("pages/my_plants.py")  # Navigate to plant selection page
with option_col2:
    st.button("My Recommendations")  # No action when clicked, as specified

st.write("")  # Adds a blank line
st.write("")  # Adds another blank line

# Navigation buttons at the bottom
nav_col1, nav_col2 = st.columns(2)
with nav_col1:
    if st.button("Back"):
        st.switch_page("pages/plant_care_options.py")  # Navigate to plant care options page
with nav_col2:
    if st.button("Home"):
        st.switch_page("app.py")  # Navigate to home page