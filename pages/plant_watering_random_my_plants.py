import streamlit as st

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("My Plants - Random")

# Initialize session state for selected plants and watering schedule
if 'selected_plants_copy' not in st.session_state:
    st.session_state.selected_plants_copy = []
if 'watering_schedule' not in st.session_state:
    st.session_state.watering_schedule = {}

# Default watering frequency (in days) for plants
default_watering_intervals = {
    "Spider Plant (Chlorophytum comosum)": 7,
    "Aloe Vera (Aloe vera)": 14,
    "Peace Lily (Spathiphyllum spp.)": 5,
    "Snake Plant (Sansevieria spp.)": 14,
    "Pothos (Epipremnum aureum)": 7,
    "Rubber Plant (Ficus elastica)": 10,
    "Swiss Cheese Plant (Monstera deliciosa)": 7,
    "Fiddle Leaf Fig (Ficus lyrata)": 7,
    "ZZ Plant (Zamioculcas zamiifolia)": 14,
    "Jade Plant (Crassula ovata)": 14,
    "English Ivy (Hedera helix)": 5,
    "Philodendron (Philodendron spp.)": 7,
    "Boston Fern (Nephrolepis exaltata)": 4,
    "Calathea (Calathea spp.)": 5,
    "Cape Jasmine (Gardenia jasminoides)": 5,
}

# 🌱 **Fix: Force UI update by creating a temporary variable**
selected_temp = st.multiselect(
    "Select your plants:",
    options=list(default_watering_intervals.keys()),
    default=st.session_state.selected_plants_copy
)

# If there's a change in selection, update session state and trigger a rerun
if selected_temp != st.session_state.selected_plants_copy:
    st.session_state.selected_plants_copy = selected_temp
    st.rerun()  # 🔄 **Forces UI update to immediately reflect new selections**

# Watering schedule input for each selected plant
for plant in st.session_state.selected_plants_copy:
    default_value = st.session_state.watering_schedule.get(plant, default_watering_intervals.get(plant, 7))
    watering_days = st.number_input(
        f"How often should {plant} be watered? (Days)",
        min_value=1, max_value=30, value=default_value
    )
    st.session_state.watering_schedule[plant] = watering_days

# Display the selected plants and their watering schedule
if st.session_state.selected_plants_copy:
    st.write("### Your Watering Schedule:")
    for plant in st.session_state.selected_plants_copy:
        st.write(f"🌱 **{plant}**: Every **{st.session_state.watering_schedule[plant]}** days")
else:
    st.write("No plants selected yet.")

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Back"):
        st.switch_page("pages/plant_watering_random.py")  

with col2:
    if st.button("Next"):
        st.switch_page("pages/plant_watering_random_notifications.py")  # Navigate to notification settings
