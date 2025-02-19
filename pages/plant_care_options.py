import streamlit as st

st.title("Plant Care Options")
col1, col2 = st.columns(2)
with col1:
    if st.button("Random"):
        st.switch_page("pages/plant_care_random.py")
with col2:
    if st.button("Personalized"):
        st.switch_page("pages/plant_care_personalized.py")