import streamlit as st

st.title("Home Screen")
st.image("Logo.png", caption="Logo")  # Assumes logo.png is in the same directory

col1, col2 = st.columns(2)
with col1:
    if st.button("Plant Watering"):
        st.switch_page("pages/plant_watering_options.py")
with col2:
    if st.button("Plant Care"):
        st.switch_page("pages/plant_care_options.py")