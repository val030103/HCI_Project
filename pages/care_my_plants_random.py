import streamlit as st

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

st.title("My Plants")

# Initialize session state
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []

# List of 10 common houseplants
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

# Multi-select widget
selected = st.multiselect(
    "Select your plants:",
    options=plants,
    default=st.session_state.selected_plants
)
st.session_state.selected_plants = selected

# Display selected plants
if selected:
    st.write("Your selected plants are:", ", ".join(selected))
else:
    st.write("No plants selected yet.")

# Bottom navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Confirm"):
        st.session_state.plants_confirmed = True  # Set the confirmation flag
        st.switch_page("pages/plant_care_random.py")
with col2:
    if st.button("Home"):
        st.switch_page("app.py")