import streamlit as st

st.title("Plant Watering Options")
col1, col2 = st.columns(2)
with col1:
    if st.button("Random"):
        st.switch_page("pages/plant_watering_random.py")
with col2:
    if st.button("Personalized"):
        st.switch_page("pages/plant_watering_personalized.py")