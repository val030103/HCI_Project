import streamlit as st

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Plant Watering - Personalized")
st.write("Track your plants' watering schedule and let the system learn when you're most likely to water them.")
st.write("Over time, your schedule will adjust to your habits, ensuring healthier plants with minimal effort.")

st.write("")  # Adds spacing

# Initialize session state for tracking simulated days
if 'days_passed' not in st.session_state:
    st.session_state.days_passed = 0  # Start at 0 days
if 'checkup_days_passed' not in st.session_state:
    st.session_state.checkup_days_passed = 0  # Used for checkup calculations
if 'watering_schedule' not in st.session_state:
    st.session_state.watering_schedule = {}  # Ensure watering schedule exists
if 'plants_notified' not in st.session_state:
    st.session_state.plants_notified = set()  # Track plants already notified

# Display the current simulated time progression
st.write(f"📅 **Days Passed:** {st.session_state.days_passed} days")

# Layout: Days input + Pass button in the same row
col1, col2 = st.columns([3, 1])  # Adjust column ratio for better spacing

with col1:
    days_to_pass = st.number_input("Enter the number of days to pass:", min_value=1, max_value=365, value=7, step=1)

with col2:
    st.write("")  # Ensures alignment
    if st.button(f"Pass {days_to_pass} Days"):
        st.session_state.days_passed += days_to_pass  # Increment the display counter
        st.session_state.checkup_days_passed += days_to_pass  # Keep checkup tracking for missed watering
        st.session_state.plants_notified.clear()  # Reset notification tracking (assume user watered them)
        st.rerun()  # Refresh to display the updated value

st.write("")  # Adds spacing

# Identify plants that need watering (but only notify once per cycle)
plants_to_water = []
for plant, interval in st.session_state.watering_schedule.items():
    if st.session_state.checkup_days_passed >= interval and plant not in st.session_state.plants_notified:
        plants_to_water.append(plant)

# Show a popup if plants need watering
if plants_to_water:
    st.warning(f"🚰 The following plants need watering: {', '.join(plants_to_water)}")
    st.session_state.plants_notified.update(plants_to_water)  # Mark plants as notified

# Custom CSS for styling buttons
st.markdown("""
    <style>
    .stButton > button {
        width: 150px; /* Uniform button width */
        height: 50px; /* Uniform button height */
        transition: all 0.3s ease; /* Smooth hover effect */
        border: 2px solid #000000;
        font-size: 18px;
    }
    .stButton > button:hover {
        color: #3b6945;
        background-color: #f0f0f0;
        border-color: #3b6945;
    }
    </style>
""", unsafe_allow_html=True)

# Arrange "My Plants", "Schedule", "Checkup" in a row
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("My Plants"):
        st.switch_page("pages/plant_watering_personalized_my_plants.py")

with col2:
    if st.button("Schedule"):
        st.switch_page("pages/plant_watering_personalized_schedule.py")

with col3:
    if st.button("Checkup"):
        st.switch_page("pages/plant_watering_personalized_checkup.py")

st.write("")  # Adds spacing

# Arrange "Back" and "Home" in a row at the bottom
col4, col5 = st.columns([1, 1])

with col4:
    if st.button("Back"):
        st.switch_page("pages/plant_watering_options.py")

with col5:
    if st.button("Home"):
        st.switch_page("app.py")
