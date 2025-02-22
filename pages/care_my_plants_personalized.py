import streamlit as st

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("My Plants")

# Initialize session state for selected plants
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []

# List of the 10 most common house plants
plants = [
    "Spider Plant (Chlorophytum comosum)",
    "Snake Plant (Sansevieria trifasciata)",
    "Pothos (Epipremnum aureum)",
    "Peace Lily (Spathiphyllum)",
    "Philodendron (Philodendron spp.)",
    "ZZ Plant (Zamioculcas zamiifolia)",
    "Rubber Plant (Ficus elastica)",
    "Aloe Vera (Aloe vera)",
    "Monstera Deliciosa",
    "Fiddle Leaf Fig (Ficus lyrata)"
]

# Multi-select widget for plant selection
selected = st.multiselect(
    "Select your plants:",
    options=plants,
    default=st.session_state.selected_plants
)

# Update session state with the user's selection
st.session_state.selected_plants = selected

# Display the selected plants
if selected:
    st.write("Your selected plants are:", ", ".join(selected))
else:
    st.write("No plants selected yet.")

# Button styling
st.markdown("""
    <style>
    .stButton > button {
        width: 150px;
        height: 50px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #000000;
    }
    .stButton > button {
        color: #000000;
        background-color: #ffffff;
    }
    .stButton > button:hover {
        color: #3b6945;
        background-color: #f0f0f0;
        border-color: #3b6945;
    }
    div.stButton > button > div > p {
        font-size: 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Confirm button sets a flag before navigating
if st.button("Confirm"):
    st.session_state.plants_confirmed_personalized = True  # Set flag for footnote
    st.switch_page("pages/plant_care_personalized.py")  # Navigate to main page