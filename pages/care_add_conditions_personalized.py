import streamlit as st

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Add Plant Conditions")

# Ensure session state for selected plants and conditions is initialized
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []
if 'plant_conditions' not in st.session_state:
    st.session_state.plant_conditions = {}

# Button styling
st.markdown("""
    <style>
    .stButton > button {
        width: 150px;
        height: 50px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #000000;
    }
    .stButton > button {
        color: #000000;
        background-color: #ffffff;
    }
    .stButton > button:hover {
        color: #3b6945;
        background-color: #f0f0f0;
        border-color: #3b6945;
    }
    div.stButton > button > div > p {
        font-size: 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Check if there are selected plants
if not st.session_state.selected_plants:
    st.write("No plants have been selected. Please go to 'My Plants' to select some.")
else:
    st.write("Select conditions for your plants:")
    # Define common plant condition options
    condition_options = [
        "Has dead leaves",
        "Looks dry",
        "Yellowing leaves",
        "Wilting",
        "Pests visible",
        "Overwatered",
        "Stunted growth"
    ]
    # For each selected plant, show a multiselect for conditions
    for plant in st.session_state.selected_plants:
        st.subheader(plant)
        # Retrieve existing conditions or default to empty list
        current_conditions = st.session_state.plant_conditions.get(plant, [])
        selected_conditions = st.multiselect(
            f"Conditions for {plant}",
            options=condition_options,
            default=current_conditions,
            key=f"conditions_{plant}"
        )
        # Update session state with selected conditions
        st.session_state.plant_conditions[plant] = selected_conditions

# Navigation button renamed to "Confirm" and sets a flag
if st.button("Confirm"):
    st.session_state.conditions_confirmed_personalized = True  # Set flag for footnote
    st.switch_page("pages/plant_care_personalized.py")  # Navigate to main page