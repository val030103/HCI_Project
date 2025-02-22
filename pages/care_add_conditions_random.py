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

st.title("Add Plant Conditions")

# Initialize session state
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []
if 'plant_conditions' not in st.session_state:
    st.session_state.plant_conditions = {}

if not st.session_state.selected_plants:
    st.write("No plants have been selected. Please go to 'My Plants' to select some.")
else:
    st.write("Select conditions for your plants:")
    condition_options = [
        "Has dead leaves", "Looks dry", "Yellowing leaves", "Wilting",
        "Pests visible", "Overwatered", "Stunted growth"
    ]
    for plant in st.session_state.selected_plants:
        st.subheader(plant)
        current_conditions = st.session_state.plant_conditions.get(plant, [])
        selected_conditions = st.multiselect(
            f"Conditions for {plant}",
            options=condition_options,
            default=current_conditions,
            key=f"conditions_{plant}"
        )
        st.session_state.plant_conditions[plant] = selected_conditions

# Bottom navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Confirm"):
        st.session_state.conditions_confirmed = True  # Set the confirmation flag
        st.switch_page("pages/plant_care_random.py")
with col2:
    if st.button("Home"):
        st.switch_page("app.py")