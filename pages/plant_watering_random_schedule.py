import streamlit as st
import pandas as pd

# Center the title
st.title("Your Plant Watering Schedule")

# Ensure session state exists
if 'selected_plants_copy' not in st.session_state or not st.session_state.selected_plants_copy:
    st.error("⚠️ No plants selected! Please go back and choose your plants first.")
    if st.button("Back"):
        st.switch_page("pages/plant_watering_random.py")
    st.stop()

# Retrieve watering times and intervals
watering_times = st.session_state.get('random_watering_times', {})
watering_intervals = st.session_state.get('watering_schedule', {})
days_passed = st.session_state.get('days_passed', 0)  # Ensure days passed exists

# Prepare data for table display
schedule_data = []
for plant in st.session_state.selected_plants_copy:
    time = watering_times.get(plant, "N/A")
    interval = watering_intervals.get(plant, "N/A")

    if isinstance(interval, int):  # Ensure valid interval
        days_until_next = interval - (days_passed % interval)
        schedule_data.append([f"🌱 {plant}", f"💧 {time}", f"📅 Every {interval} days", f"⏳ Due in {days_until_next} days"])
    else:
        schedule_data.append([f"🌱 {plant}", f"💧 {time}", f"📅 Invalid Interval", "❌"])

# Convert to DataFrame
df = pd.DataFrame(schedule_data, columns=["Plant", "Watering Time", "Interval", "Next Watering"])

# Display table
st.write("### Your Watering Schedule")
st.table(df)

# Navigation button
if st.button("Back"):
    st.switch_page("pages/plant_watering_random.py")
