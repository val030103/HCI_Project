import streamlit as st
import random

# Center the title and define button styles
st.markdown("""
    <style>
    h1 { text-align: center; }
    .stButton > button {
        width: 150px; height: 50px; margin: 10px auto; display: block;
        transition: all 0.3s ease; border: 2px solid #000000;
        color: #000000; background-color: #ffffff;
    }
    .stButton > button:hover {
        color: #3b6945; background-color: #f0f0f0; border-color: #3b6945;
    }
    div.stButton > button > div > p { font-size: 24px !important; }
    </style>
""", unsafe_allow_html=True)

st.title("My Recommendations - Random")

# Initialize session state
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []
if 'day_counter' not in st.session_state:
    st.session_state.day_counter = 0

# General recommendations
general_recommendations = [
    "Water when the top inch of soil feels dry.",
    "Provide 6 hours of indirect sunlight daily.",
    "Rotate every few weeks for even growth.",
    "Fertilize every 4-6 weeks during growing season.",
    "Wipe leaves to remove dust.",
    "Check for pests regularly.",
    "Keep away from drafts.",
    "Mist to increase humidity.",
    "Prune dead leaves.",
    "Use pots with drainage holes."
]

if not st.session_state.selected_plants:
    st.write("No plants have been selected. Please go to 'My Plants' to select some.")
else:
    st.write("Here are random general recommendations for your plants:")
    random.seed(st.session_state.day_counter)  # Seed based on day counter
    for plant in st.session_state.selected_plants:
        st.subheader(plant)
        recommendation = random.choice(general_recommendations)
        st.write(recommendation)

# Bottom navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Back"):
        st.switch_page("pages/plant_care_random.py")
with col2:
    if st.button("Home"):
        st.switch_page("app.py")