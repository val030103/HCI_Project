import streamlit as st
import random

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("My Recommendations - Personalized")

# Ensure session state for selected plants, conditions, and feedback is initialized
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []
if 'plant_conditions' not in st.session_state:
    st.session_state.plant_conditions = {}
if 'plant_feedback' not in st.session_state:
    st.session_state.plant_feedback = {}

# Button styling
st.markdown("""
    <style>
    .stButton > button {
        width: 150px;
        height: 50px;
        margin-top: 10px auto;
        display: block;
        transition: all 0.3s ease;
        border: 2px solid #000000;
        margin-left: -22px:
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

# Define condition-based recommendations
condition_recommendations = {
    "Has dead leaves": [
        "Prune the dead leaves to encourage new growth.",
        "Check if the plant is getting enough light.",
        "Ensure the plant is not overwatered or underwatered."
    ],
    "Looks dry": [
        "Increase watering frequency, but ensure proper drainage.",
        "Mist the plant to increase humidity.",
        "Check if the plant is in a location with low humidity."
    ],
    "Yellowing leaves": [
        "Yellow leaves can indicate overwatering; reduce watering frequency.",
        "Ensure the plant is not in direct sunlight, which can scorch leaves.",
        "Check for nutrient deficiencies; consider fertilizing."
    ],
    "Wilting": [
        "Wilting can be a sign of underwatering; water the plant thoroughly.",
        "Check if the plant is root-bound and needs repotting.",
        "Ensure the plant is not exposed to extreme temperatures."
    ],
    "Pests visible": [
        "Isolate the plant to prevent pests from spreading.",
        "Use insecticidal soap or neem oil to treat the infestation.",
        "Regularly inspect and clean the leaves."
    ],
    "Overwatered": [
        "Allow the soil to dry out before watering again.",
        "Ensure the pot has proper drainage.",
        "Consider repotting with fresh, well-draining soil."
    ],
    "Stunted growth": [
        "Check if the plant needs more light or a larger pot.",
        "Ensure it's receiving adequate nutrients; fertilize if necessary.",
        "Verify that the temperature and humidity are suitable."
    ]
}

# Define plant-specific recommendations for the 10 most common house plants
plant_recommendations = {
    "Spider Plant (Chlorophytum comosum)": {
        "base": [
            "Provide bright, indirect light.",
            "Allow soil to dry between waterings.",
            "Maintain moderate humidity.",
            "Prune dead leaves regularly.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Check for overwatering; ensure proper drainage.",
            "Increase light exposure if leaves are pale.",
            "Inspect for pests like spider mites."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for any changes in leaf color or growth."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider propagating plantlets for new plants."
        ]
    },
    "Snake Plant (Sansevieria trifasciata)": {
        "base": [
            "Tolerates low to bright indirect light.",
            "Water sparingly; allow soil to dry completely.",
            "Prefers low humidity.",
            "Avoid overwatering to prevent root rot.",
            "Clean leaves regularly to remove dust."
        ],
        "poor": [
            "Reduce watering frequency; check for root rot.",
            "Ensure the pot has good drainage.",
            "Move to a brighter location if leaves are drooping."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for signs of overwatering."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider repotting if the plant outgrows its container."
        ]
    },
    "Pothos (Epipremnum aureum)": {
        "base": [
            "Thrives in low to bright indirect light.",
            "Allow soil to dry between waterings.",
            "Maintain moderate humidity.",
            "Prune to control growth and encourage bushiness.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Check for underwatering if leaves are wilting.",
            "Increase light if growth is leggy.",
            "Inspect for pests like mealybugs."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for yellowing leaves."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider propagating cuttings for new plants."
        ]
    },
    "Peace Lily (Spathiphyllum)": {
        "base": [
            "Prefers low to medium indirect light.",
            "Keep soil consistently moist but not soggy.",
            "Maintain high humidity; mist leaves regularly.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Increase watering if leaves are drooping.",
            "Provide more humidity if leaf tips are browning.",
            "Check for pests like aphids."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for flower production."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider dividing the plant if it becomes root-bound."
        ]
    },
    "Philodendron (Philodendron spp.)": {
        "base": [
            "Thrives in medium to bright indirect light.",
            "Allow soil to dry between waterings.",
            "Maintain moderate humidity.",
            "Prune to control growth.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Check for overwatering if leaves are yellowing.",
            "Increase light if growth is slow.",
            "Inspect for pests like scale."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for new growth."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider propagating stem cuttings."
        ]
    },
    "ZZ Plant (Zamioculcas zamiifolia)": {
        "base": [
            "Tolerates low to bright indirect light.",
            "Water sparingly; allow soil to dry completely.",
            "Prefers low humidity.",
            "Avoid overwatering to prevent root rot.",
            "Clean leaves regularly."
        ],
        "poor": [
            "Reduce watering frequency; check for root rot.",
            "Ensure good drainage.",
            "Move to a brighter location if leaves are yellowing."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for signs of overwatering."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider repotting if necessary."
        ]
    },
    "Rubber Plant (Ficus elastica)": {
        "base": [
            "Provide bright indirect light.",
            "Allow soil to dry between waterings.",
            "Maintain moderate humidity.",
            "Prune to control growth.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Check for underwatering if leaves are dropping.",
            "Increase light if leaves are losing color.",
            "Inspect for pests like spider mites."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for new leaf growth."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider propagating from stem cuttings."
        ]
    },
    "Aloe Vera (Aloe vera)": {
        "base": [
            "Requires bright direct light.",
            "Water sparingly; allow soil to dry completely.",
            "Prefers low humidity.",
            "Ensure good drainage to prevent root rot."
        ],
        "poor": [
            "Reduce watering frequency; check for root rot.",
            "Move to a sunnier spot if leaves are stretching.",
            "Inspect for pests like mealybugs."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for gel production in leaves."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider harvesting gel for use."
        ]
    },
    "Monstera Deliciosa": {
        "base": [
            "Provide bright indirect light.",
            "Allow soil to dry between waterings.",
            "Maintain high humidity.",
            "Provide support for climbing.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Check for overwatering if leaves are yellowing.",
            "Increase humidity if leaf edges are browning.",
            "Inspect for pests like thrips."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for new leaf splits."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider propagating from stem cuttings."
        ]
    },
    "Fiddle Leaf Fig (Ficus lyrata)": {
        "base": [
            "Provide bright indirect light.",
            "Allow soil to dry between waterings.",
            "Maintain moderate humidity.",
            "Rotate plant regularly for even growth.",
            "Fertilize monthly during the growing season."
        ],
        "poor": [
            "Check for underwatering if leaves are browning.",
            "Adjust light exposure if leaves are dropping.",
            "Inspect for pests like spider mites."
        ],
        "moderate": [
            "Maintain current care routine.",
            "Monitor for new leaf growth."
        ],
        "high": [
            "Continue with current care routine.",
            "Consider repotting if root-bound."
        ]
    }
}

# Function to calculate plant condition based on feedback
def calculate_condition(feedback):
    if len(feedback) >= 3:
        avg_rating = sum(feedback[-3:]) / 3
        if avg_rating < 3:
            return "poor"
        elif avg_rating == 3:
            return "moderate"
        else:
            return "high"
    elif feedback:
        last_rating = feedback[-1]
        if last_rating < 3:
            return "poor"
        elif last_rating == 3:
            return "moderate"
        else:
            return "high"
    else:
        return "moderate"  # Default if no feedback

# Check if there are selected plants
if not st.session_state.selected_plants:
    st.write("No plants have been selected. Please go to 'My Plants' to select some.")
else:
    st.write("Here are personalized recommendations for your selected plants:")
    for plant in st.session_state.selected_plants:
        st.subheader(plant)
        conditions = st.session_state.plant_conditions.get(plant, [])
        feedback = st.session_state.plant_feedback.get(plant, [])

        # Determine plant condition based on feedback
        condition = calculate_condition(feedback)

        # Display condition-based recommendations
        if conditions:
            st.write("Based on the selected conditions:")
            for cond in conditions:
                st.write(f"- {cond}:")
                recommendations = condition_recommendations.get(cond, ["No specific recommendations available."])
                for rec in recommendations:
                    st.write(f"  - {rec}")

        # Display plant-specific base recommendations
        st.write("General care tips:")
        base_recs = plant_recommendations.get(plant, {}).get("base", ["No specific recommendations available."])
        for rec in base_recs:
            st.write(f"- {rec}")

        # Display feedback-based recommendations
        if feedback:
            st.write("Based on your feedback:")
            if condition == "poor":
                st.write("Your plant seems to be struggling. Consider the following adjustments:")
            elif condition == "moderate":
                st.write("Your plant is doing okay. Here are some tips to maintain its health:")
            elif condition == "high":
                st.write("Your plant is thriving! Keep up the good work with these suggestions:")

            conditional_recs = plant_recommendations.get(plant, {}).get(condition, ["No specific recommendations available."])
            for rec in conditional_recs:
                st.write(f"- {rec}")
        else:
            st.write("No feedback provided yet. Please rate your plant's condition daily for personalized recommendations.")

# Navigation buttons
nav_col1, nav_col2 = st.columns(2)
with nav_col1:
    if st.button("Back"):
        st.switch_page("pages/plant_care_personalized.py")  # Return to personalized main page