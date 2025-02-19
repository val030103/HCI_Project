import streamlit as st

st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Plant Care Buddy App")

st.image("Logo.png", width=600)

# Custom CSS to increase button size
st.markdown("""
    <style>
    .stButton > button {
        width: 200px;  /* Button width */
        height: 60px;  /* Button height */
        margin: 10px auto;  /* Center buttons within their columns */
        display: block;  /* Ensure centering works */
        margin-left: 5x;
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

# Five columns: adjusted to center buttons
col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 2, 1])  # Adjusted ratios
with col2:  # Left of center
    if st.button("Plant Watering"):
        st.switch_page("pages/plant_watering_options.py")
with col4:  # Right of center
    if st.button("Plant Care"):
        st.switch_page("pages/plant_care_options.py")