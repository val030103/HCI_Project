import streamlit as st

# Center the title and define enhanced styles, including footnote styling, separate Home button settings, and hardcoded margins
st.markdown("""
    <style>
    h1 {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 20px;
    }
    .stButton > button {
        width: 200px;  /* Default button width for other buttons (e.g., Back, Next Day) */
        height: 50px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #000000;
        font-size: 20px !important;  /* Larger button text for readability */
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
        font-size: 20px !important;  /* Ensure button text size is consistent */
    }
    /* Target specific confirm rating buttons by their keys (e.g., confirm_<plant>_<day_counter>) */
    [data-testid="stButton"][key^="confirm_"] > button {
        width: 300px !important;  /* Larger width for plant-specific confirm buttons */
        height: 50px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #000000;
        font-size: 20px !important;
    }
    [data-testid="stButton"][key^="confirm_"] > button {
        color: #000000;
        background-color: #ffffff;
    }
    [data-testid="stButton"][key^="confirm_"] > button:hover {
        color: #3b6945;
        background-color: #f0f0f0;
        border-color: #3b6945;
    }
    [data-testid="stButton"][key^="confirm_"] > button > div > p {
        font-size: 20px !important;  /* Ensure button text size is consistent */
    }
    /* Specific styling for the Home button (key="home_button") with hardcoded margins */
    [data-testid="stButton"][key="home_button"] > button {
        width: 200px;  /* Maintain default width */
        height: 50px;
        margin: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #1e90ff;  /* Distinct blue border for Home button */
        font-size: 20px !important;
        background-color: #ffffff;
    }
    [data-testid="stButton"][key="home_button"] > button {
        color: #000000;
    }
    [data-testid="stButton"][key="home_button"] > button:hover {
        color: #ffffff;  /* White text on hover for contrast */
        background-color: #1e90ff;  /* Blue background on hover for distinction */
        border-color: #1e90ff;
    }
    [data-testid="stButton"][key="home_button"] > button > div > p {
        font-size: 20px !important;  /* Ensure button text size is consistent */
    }
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
    /* Style for general text and headers */
    .stMarkdown {
        margin-bottom: 15px;
        font-size: 16px;
        color: #34495e;
    }
    /* Style for subheaders (Day counter) */
    h3 {
        text-align: center;
        font-size: 24px;
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 15px;
    }
    /* Add a distinct separator line */
    hr {
        border: 2px solid #e0e0e0;
        margin: 25px 0;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Plant Care - V2")

# Initialize session state
if 'day_counter' not in st.session_state:
    st.session_state.day_counter = 0
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []
if 'plant_feedback' not in st.session_state:
    st.session_state.plant_feedback = {plant: [] for plant in st.session_state.selected_plants}
if 'temp_ratings' not in st.session_state:
    st.session_state.temp_ratings = {}
if 'show_rating_menu' not in st.session_state:
    st.session_state.show_rating_menu = {}
if 'ratings_confirmed_personalized' not in st.session_state:
    st.session_state.ratings_confirmed_personalized = False

# Navigation options with improved spacing and centered logos
st.markdown('<p class="stMarkdown">Choose an option:</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    # Wrap st.image in a centered div
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("MyPlants_logo.png", width=60, output_format="auto")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("My Plants", key="my_plants_button"):
        st.switch_page("pages/care_my_plants_personalized.py")

with col2:
    # Wrap st.image in a centered div
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("Condition_logo.png", width=60, output_format="auto")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Add Conditions", key="add_conditions_button"):
        st.switch_page("pages/care_add_conditions_personalized.py")

with col3:
    # Wrap st.image in a centered div
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("Recommendations_logo.png", width=60, output_format="auto")
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Recommendations", key="recommendations_button"):
        st.switch_page("pages/care_my_recommendations_personalized.py")

# Day counter and feedback section with enhanced separator
st.markdown('<hr>', unsafe_allow_html=True)
st.subheader(f"Day {st.session_state.day_counter}")
if not st.session_state.selected_plants:
    st.markdown('<p class="stMarkdown">No plants selected yet. Please go to \'My Plants\' to add some.</p>', unsafe_allow_html=True)
else:
    # Center the "Next Day" button for better alignment
    col_next_day, _, _ = st.columns([1, 2, 1])  # Center the button using columns
    with col_next_day:
        if st.button("Next Day"):
            st.session_state.day_counter += 1
            for plant in st.session_state.selected_plants:
                st.session_state.show_rating_menu[plant] = True
                st.session_state.temp_ratings[plant] = 0  # Default rating

    # Rating section for each plant
    # Only show the message if at least one rating menu is visible
    if any(st.session_state.show_rating_menu.get(plant, False) for plant in st.session_state.selected_plants):
        st.markdown('<p class="stMarkdown">Please rate each plant and confirm your selection:</p>', unsafe_allow_html=True)
    
    for plant in st.session_state.selected_plants:
        if st.session_state.show_rating_menu.get(plant, False):
            st.markdown(f'<h4 style="color: #2c3e50; margin-top: 15px;">Rate {plant}</h4>', unsafe_allow_html=True)
            rating = st.radio(
                f"Select rating for {plant}",
                options=[0, 1, 2, 3, 4, 5],
                format_func=lambda x: '★' * x + '☆' * (5 - x),
                key=f"rating_{plant}_{st.session_state.day_counter}",
                index=st.session_state.temp_ratings.get(plant, 0)
            )
            st.session_state.temp_ratings[plant] = rating
            # Use default button styling, but CSS targets it by key for width
            if st.button("Confirm Rating", key=f"confirm_{plant}_{st.session_state.day_counter}"):
                if plant not in st.session_state.plant_feedback:
                    st.session_state.plant_feedback[plant] = []
                st.session_state.plant_feedback[plant].append(rating)
                st.session_state.show_rating_menu[plant] = False
                # Check if all ratings are confirmed for the day
                if all(not st.session_state.show_rating_menu.get(p, False) for p in st.session_state.selected_plants):
                    st.session_state.ratings_confirmed_personalized = True

st.markdown('<hr>', unsafe_allow_html=True)  # Add separator before navigation buttons

# Navigation buttons with hardcoded margins for Home button
nav_col1, nav_col2, nav_col3 = st.columns(3)
with nav_col1:
    if st.button("Back"):
        st.switch_page("pages/plant_care_options.py")
with nav_col3:
    if st.button("Home", key="home_button"):
        st.switch_page("app.py")

# Display confirmation footnotes with fade-out animation
if 'plants_confirmed_personalized' in st.session_state and st.session_state.plants_confirmed_personalized:
    st.markdown(
        '<p class="footnote">🌱 Plants added successfully. <br>A new recommendation is now available in the \'Recommendations\' space.</p>',
        unsafe_allow_html=True
    )
    st.markdown("""
        <script>
        setTimeout(function() {
            var footnote = document.querySelector('.footnote');
            if (footnote) {
                footnote.style.display = 'none';
            }
        }, 5000);
        </script>
    """, unsafe_allow_html=True)
    del st.session_state.plants_confirmed_personalized

if 'conditions_confirmed_personalized' in st.session_state and st.session_state.conditions_confirmed_personalized:
    st.markdown(
        '<p class="footnote">✓ Conditions saved successfully.</p>',
        unsafe_allow_html=True
    )
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
    del st.session_state.conditions_confirmed_personalized

if 'ratings_confirmed_personalized' in st.session_state and st.session_state.ratings_confirmed_personalized:
    st.markdown(
        '<p class="footnote">✓ A new recommendation is now available in the \'Recommendations\' space.</p>',
        unsafe_allow_html=True
    )
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
    st.session_state.ratings_confirmed_personalized = False