import streamlit as st
import random
import time as t  # Use t instead of time to avoid conflicts

# Center the title
st.title("Notifications")

# Ensure user has selected plants
if 'selected_plants_copy' not in st.session_state or not st.session_state.selected_plants_copy:
    st.error("⚠️ No plants selected! Please go back and choose your plants first.")
    if st.button("Back"):
        st.switch_page("pages/plant_watering_random_my_plants.py")
    st.stop()

# Get selected plants from session state
selected_plants = st.session_state.selected_plants_copy

if 'random_watering_times' not in st.session_state:
    st.session_state.random_watering_times = {}  # Ensure the dictionary exists

available_times = [
    f"{hour}:{minute}"
    for hour in range(14, 21)  # 2 PM to 8 PM
    for minute in ["00", "15", "30", "45"]
]
random.shuffle(available_times)  # Shuffle to distribute randomly

# Assign times only to new plants
for plant in selected_plants:
    if plant not in st.session_state.random_watering_times:
        st.session_state.random_watering_times[plant] = available_times[len(st.session_state.random_watering_times) % len(available_times)]


# Ask user for notification type
st.write("### Notification Type")
notification_options = ["Push Notification", "Email", "SMS"]
st.session_state.notification_type = st.selectbox("📩 How do you want to receive reminders?", 
                                                  notification_options, 
                                                  index=notification_options.index(st.session_state.get("notification_type", "Push Notification")))

# Display assigned watering times for all selected plants
st.write("### Your Assigned Watering Times")
for plant in selected_plants:
    watering_time = st.session_state.random_watering_times.get(plant, "N/A")
    st.write(f"🌱 **{plant}** → 💧 Water at **{watering_time}**")

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Back"):
        st.switch_page("pages/plant_watering_random_my_plants.py")

with col2:
    if st.button("Finish"):
        st.session_state["plants_saved"] = True  # Set flag for confirmation
        st.rerun()  # Refresh the page to show the confirmation messages

# Show confirmation message before switching pages
if st.session_state.get("plants_saved"):
    st.success("✅ Your plants have been saved! Redirecting... 🌱")
    t.sleep(2)  # Wait 2 seconds so the user sees the message
    del st.session_state["plants_saved"]  # Remove flag to prevent repeated messages
    st.switch_page("pages/plant_watering_random.py")  # Redirect after message
