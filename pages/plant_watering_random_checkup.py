import streamlit as st
import random
import time  # Import time for sleep

# Center the title
st.title("Plant Watering - Checkup")

# Ensure session state exists
if 'selected_plants_copy' not in st.session_state:
    st.session_state.selected_plants_copy = []
if 'random_watering_times' not in st.session_state:
    st.session_state.random_watering_times = {}
if 'watering_schedule' not in st.session_state:
    st.session_state.watering_schedule = {}
if 'checkup_confirmed' not in st.session_state:
    st.session_state.checkup_confirmed = False  # Track confirmation status
if 'checkup_days_passed' not in st.session_state:
    st.session_state.checkup_days_passed = 0  # Used for checkup calculations
if 'updated_watering_times' not in st.session_state:
    st.session_state.updated_watering_times = {}  # Store updated watering times only after confirmation

# Get the number of days that have passed since the last checkup
days_since_last_checkup = st.session_state.checkup_days_passed

# Identify plants that should have been watered at least once during the elapsed time
plants_due_for_watering = []
for plant, interval in st.session_state.watering_schedule.items():
    if days_since_last_checkup >= interval:  # If full cycle(s) passed
        plants_due_for_watering.append(plant)

# Select plants that were missed
st.write("Which plants did you **miss** watering?")
missed_plants = st.multiselect(
    "Select the plants:",
    options=plants_due_for_watering  # Only show plants that should have been watered
)

# Generate new random watering times for missed plants
new_watering_times = {}
for plant in missed_plants:
    new_hour = random.randint(14, 20)  # Between 2 PM and 8 PM
    new_minute = random.choice(["00", "15", "30", "45"])
    new_watering_times[plant] = f"{new_hour}:{new_minute}"

# Confirm button updates the schedule
if st.button("Confirm"):
    if 'random_watering_times' not in st.session_state:
        st.session_state.random_watering_times = {}  # Ensure the key exists
    
    # Update session state with new times
    st.session_state.random_watering_times.update(new_watering_times)
    st.session_state.updated_watering_times = new_watering_times  # Store updated times for display

    # Reset checkup_days_passed to 0 since we completed a checkup
    st.session_state.checkup_days_passed = 0  

    # Store confirmation flag
    st.session_state.checkup_confirmed = True

    st.success("✅ Your watering schedule has been updated! Redirecting... 🌱")

    # Delay before switching page
    time.sleep(2)

    # Redirect after confirmation
    st.switch_page("pages/plant_watering_random.py")

# Only show the updated times AFTER confirmation
if st.session_state.checkup_confirmed and st.session_state.updated_watering_times:
    st.write("### Latest Schedule Changes:")
    for plant, time in st.session_state.updated_watering_times.items():
        st.write(f"🌱 **{plant}** → 💧 New watering time: **{time}**")

# Navigation buttons
if st.button("Back"):
    st.switch_page("pages/plant_watering_random.py")