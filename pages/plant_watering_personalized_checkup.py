import streamlit as st
import random
import time  # Import time for sleep
from datetime import datetime, timedelta

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
if 'missed_time_counts' not in st.session_state:
    st.session_state.missed_time_counts = {}  # Count how often a time was missed
if 'good_time_suggestions' not in st.session_state:
    st.session_state.good_time_suggestions = {}  # Track good times for each plant

# Function to check if a time falls within ±15 minutes of another time
def is_within_range(target_time, reference_time):
    """Check if target_time falls within ±15 minutes of reference_time."""
    target_dt = datetime.strptime(target_time, "%H:%M")
    reference_dt = datetime.strptime(reference_time, "%H:%M")
    return abs((target_dt - reference_dt).total_seconds()) <= 15 * 60  # 15 minutes in seconds

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

# Identify plants that were NOT marked as missed (good time suggestion)
good_time_plants = [plant for plant in plants_due_for_watering if plant not in missed_plants]

# Generate new watering times based on user behavior (only after confirmation)
new_watering_times = {}

if st.button("Confirm"):
    if 'random_watering_times' not in st.session_state:
        st.session_state.random_watering_times = {}  # Ensure the key exists

    # Generate new watering times for missed plants
    for plant in missed_plants:
        previous_time = st.session_state.random_watering_times.get(plant)

        # Increase the count of how often a time in the missed range was missed
        if previous_time:
            for stored_time in list(st.session_state.missed_time_counts.keys()):
                if is_within_range(previous_time, stored_time):
                    st.session_state.missed_time_counts[stored_time] += 1
                    break
            else:
                st.session_state.missed_time_counts[previous_time] = 1

        # Reduce the likelihood of suggesting the previously missed time range
        while True:
            new_hour = random.randint(14, 20)  # Between 2 PM and 8 PM
            new_minute = random.choice(["00", "15", "30", "45"])
            suggested_time = f"{new_hour}:{new_minute}"

            # Check if the new time falls into a bad or good category
            missed_count = sum(1 for missed_time in st.session_state.missed_time_counts.keys() 
                               if is_within_range(suggested_time, missed_time))
            good_count = sum(1 for good_time in st.session_state.good_time_suggestions.keys() 
                             if is_within_range(suggested_time, good_time))

            # Weight the suggestion based on learning data
            if missed_count == 0:  # If not missed, allow it
                break
            elif good_count > missed_count:  # If it was followed more than missed, suggest it
                if random.random() < 0.7:  # 70% chance to accept
                    break
            elif missed_count > good_count:  # If missed more than followed, avoid it
                if random.random() < 0.3:  # 30% chance to accept
                    break

        new_watering_times[plant] = suggested_time

    # Reinforce "good" times for plants that were NOT marked as missed
    for plant in good_time_plants:
        last_time = st.session_state.random_watering_times.get(plant)
        if last_time:
            for stored_time in list(st.session_state.good_time_suggestions.keys()):
                if is_within_range(last_time, stored_time):
                    st.session_state.good_time_suggestions[stored_time] += 1  # Increase weight
                    break
            else:
                st.session_state.good_time_suggestions[last_time] = 1  # Store new good time

    # Update session state with new times
    st.session_state.random_watering_times.update(new_watering_times)
    st.session_state.updated_watering_times = new_watering_times  # Store updated times for display

    # Reset `checkup_days_passed` to 0 since we completed a checkup
    st.session_state.checkup_days_passed = 0  

    # Store confirmation flag
    st.session_state.checkup_confirmed = True

    st.success("✅ Your watering schedule has been updated! Learning from your availability... 🌱")

    # Delay before switching page
    time.sleep(2)

    # Redirect after confirmation
    st.switch_page("pages/plant_watering_personalized.py")

# Only show the updated times AFTER confirmation
if st.session_state.checkup_confirmed and st.session_state.updated_watering_times:
    st.write("### Latest Schedule Changes:")
    for plant, time in st.session_state.updated_watering_times.items():
        st.write(f"🌱 **{plant}** → 💧 New watering time: **{time}**")



# Navigation buttons
if st.button("Back"):
    st.switch_page("pages/plant_watering_personalized.py")
