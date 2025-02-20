import streamlit as st

st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)
st.title("Plant Care Options")

st.write("")
st.write("")

col1, col2 = st.columns(2)
with col1:
    if st.button("Random"):
        st.switch_page("pages/plant_care_random.py")
with col2:
    if st.button("Personalized"):
        st.switch_page("pages/plant_care_personalized.py")

st.write("")  # Adds a blank line
st.write("")  # Adds another blank line

st.markdown("""
    <style>
    .stButton > button {
        width: 160px;  /* Button width */
        height: 50px;  /* Button height */
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

# Back button at the bottom
if st.button("Back"):
    st.switch_page("app.py")  # Navigate back to the home page