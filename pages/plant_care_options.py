import streamlit as st

# Center the title using CSS
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Plant Care Options")

# Top buttons: Random and Personalized
col1, col2 = st.columns(2)
with col1:
    if st.button("Random"):
        st.switch_page("pages/plant_care_random.py")
with col2:
    if st.button("Personalized"):
        st.switch_page("pages/plant_care_personalized.py")

# Horizontal line separator
st.markdown("<hr>", unsafe_allow_html=True)

# Bottom buttons: Back and Reset All
col3, col4 = st.columns(2)
with col3:
    if st.button("Back"):
        st.switch_page("app.py")  # Navigate back to the home page
with col4:
    if st.button("Reset All", key="reset_all_button"):
        # Reset metrics for both Random and Personalized options
        st.session_state.selected_plants = []
        st.session_state.day_counter = 0
        st.session_state.plant_conditions = {}
        st.session_state.plant_feedback = {}
        st.session_state.temp_ratings = {}
        st.session_state.show_rating_menu = {}
        st.session_state.reset_confirmed = True  # Flag to show confirmation
        st.rerun()

# Apply button styling and add footnote styling with fade-out animation
st.markdown("""
    <style>
    .stButton > button {
        width: 160px;  /* Button width */
        height: 50px;  /* Button height */
        margin: 10px auto;  /* Center buttons within their columns */
        display: block;  /* Ensure centering works */
        transition: all 0.3s ease;  /* Smooth transition for hover effect */
        border: 2px solid #000000;  /* Default border */
    }
    /* Normal state */
    .stButton > button {
        color: #000000;  /* Default text color */
        background-color: #ffffff;  /* Default background */
    }
    /* Hover state */
    .stButton > button:hover {
        color: #3b6945;  /* Text color on hover */
        background-color: #f0f0f0;  /* Background color on hover */
        border-color: #3b6945;  /* Border color on hover */
    }
    div.stButton > button > div > p {
        font-size: 24px !important;  /* Adjust size */
    }
    /* Footnote styling with fade-out animation */
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

# Display confirmation footnote with fade-out if reset was successful
if 'reset_confirmed' in st.session_state and st.session_state.reset_confirmed:
    st.markdown(
        '<p class="footnote">✓ Reset successful: All metrics have been cleared.</p>',
        unsafe_allow_html=True
    )
    # Inject JavaScript to remove the footnote after animation
    st.markdown("""
        <script>
        setTimeout(function() {
            var footnote = document.querySelector('.footnote');
            if (footnote) {
                footnote.style.display = 'none';
            }
        }, 3000);
        </script>
    """, unsafe_allow_html=True)
    # Reset the flag after displaying to prevent re-rendering
    del st.session_state.reset_confirmed