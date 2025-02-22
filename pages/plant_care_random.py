import streamlit as st

# Apply CSS styling to match the personalized main page
st.markdown("""
    <style>
    /* Title styling */
    h1 {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    /* Button styling */
    .stButton > button {
        width: 200px;
        height: 50px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #000000;
        color: #000000;
        background-color: #ffffff;
    }
    .stButton > button:hover {
        color: #3b6945;
        background-color: #f0f0f0;
        border-color: #3b6945;
    }
    div.stButton > button > div > p {
        font-size: 20px !important;
    }
    /* General text (instructions, messages) */
    .stMarkdown {
        margin-bottom: 15px;
        font-size: 16px;
        color: #34495e;
        text-align: center;
    }
    /* Day counter */
    h3 {
        text-align: center;
        font-size: 24px;
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    /* Horizontal lines */
    hr {
        border: 2px solid #e0e0e0;
        margin: 25px 0;
    }
    /* Footnote styling (if applicable) */
    .footnote {
        font-size: 12px;
        color: #666666;
        text-align: center;
        margin-top: 20px;
        animation: fadeOut 3s forwards;
    }
    @keyframes fadeOut {
        0% { opacity: 1; }
        80% { opacity: 1; }
        100% { opacity: 0; }
    }
    </style>
""", unsafe_allow_html=True)

# Set title
st.title("Plant Care - Random")

# Initialize session state
if 'day_counter' not in st.session_state:
    st.session_state.day_counter = 0
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []
if 'plant_conditions' not in st.session_state:
    st.session_state.plant_conditions = {}

# Instruction text
st.markdown('<p class="stMarkdown">Choose an option:</p>', unsafe_allow_html=True)

# Top buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("My Plants"):
        st.switch_page("pages/care_my_plants_random.py")
with col2:
    if st.button("Add Conditions"):
        st.switch_page("pages/care_add_conditions_random.py")
with col3:
    if st.button("Recommendations"):
        st.switch_page("pages/care_my_recommendations_random.py")

# First horizontal line
st.markdown("<hr>", unsafe_allow_html=True)

# Day counter
st.subheader(f"Day {st.session_state.day_counter}")

# Conditional display of message or Next Day button
if not st.session_state.selected_plants:
    st.markdown('<p class="stMarkdown">No plants selected yet. Please go to \'My Plants\' to add some.</p>', unsafe_allow_html=True)
else:
    if st.button("Next Day"):
        st.session_state.day_counter += 1
        st.session_state.recommendation_available = True
        st.rerun()

# Second horizontal line
st.markdown("<hr>", unsafe_allow_html=True)

# Bottom buttons
nav_col1, nav_col2, nav_col3 = st.columns(3)
with nav_col1:
    if st.button("Back"):
        st.switch_page("pages/plant_care_options.py")
with nav_col3:
    if st.button("Home"):
        st.switch_page("app.py")

# Display confirmation footnotes (if applicable)
# ... (keep existing footnote code if present)