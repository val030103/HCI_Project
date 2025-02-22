import streamlit as st

# Center the title
st.markdown("""
    <style>
    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("My Plants")

# Initialize session state for selected plants and watering schedule
if 'selected_plants_copy' not in st.session_state:
    st.session_state.selected_plants_copy = []
if 'watering_schedule' not in st.session_state:
    st.session_state.watering_schedule = {}

# Realistic watering frequency (in days) based on plant type
default_watering_intervals = {
    "Spider Plant (Chlorophytum comosum)": 7,
    "Aloe Vera (Aloe vera)": 14,
    "Peace Lily (Spathiphyllum spp.)": 5,
    "Snake Plant (Sansevieria spp.)": 14,
    "Pothos (Epipremnum aureum)": 7,
    "Rubber Plant (Ficus elastica)": 10,
    "Swiss Cheese Plant (Monstera deliciosa)": 7,
    "Fiddle Leaf Fig (Ficus lyrata)": 7,
    "ZZ Plant (Zamioculcas zamiifolia)": 14,
    "Jade Plant (Crassula ovata)": 14,
    "English Ivy (Hedera helix)": 5,
    "Philodendron (Philodendron spp.)": 7,
    "Moth Orchid (Phalaenopsis spp.)": 10,
    "Boston Fern (Nephrolepis exaltata)": 4,
    "Parlour Palm (Chamaedorea elegans)": 7,
    "Yucca (Yucca spp.)": 14,
    "African Violet (Saintpaulia spp.)": 5,
    "Chinese Money Plant (Pilea peperomioides)": 7,
    "Dragon Tree (Dracaena draco)": 10,
    "Weeping Fig (Ficus benjamina)": 7,
    "Prayer Plant (Maranta leuconeura)": 5,
    "String of Pearls (Senecio rowleyanus)": 14,
    "Areca Palm (Dypsis lutescens)": 7,
    "Dumb Cane (Dieffenbachia spp.)": 7,
    "Venus Flytrap (Dionaea muscipula)": 5,
    "Maidenhair Fern (Adiantum spp.)": 4,
    "Poinsettia (Euphorbia pulcherrima)": 7,
    "Amaryllis (Hippeastrum spp.)": 10,
    "Flamingo Flower (Anthurium andraeanum)": 7,
    "Bird's Nest Fern (Asplenium nidus)": 5,
    "Polka Dot Plant (Hypoestes phyllostachya)": 5,
    "Corn Plant (Dracaena fragrans)": 10,
    "Calathea (Calathea spp.)": 5,
    "Heart Leaf Philodendron (Philodendron hederaceum)": 7,
    "Sword Fern (Polystichum munitum)": 4,
    "Cape Jasmine (Gardenia jasminoides)": 5,
    "Tiger Aloe (Aloe variegata)": 14,
    "Velvet Plant (Gynura aurantiaca)": 7,
    "Dwarf Umbrella Tree (Schefflera arboricola)": 7,
    "Flaming Katy (Kalanchoe blosseldiana)": 10,
    "Zebra Plant (Haworthia fasciata)": 14,
    "Sensitive Plant (Mimosa pudica)": 5,
    "Silver Inch Plant (Tradescantia zebrina)": 7,
    "Living Stones (Lithops spp.)": 21,
    "Pink Quill (Tillandsia cyanea)": 10,
    "Madagascar Jasmine (Stephanotis floribunda)": 7,
    "Joseph's Coat (Codiaeum variegatum)": 10,
    "Cape Primrose (Streptocarpus spp.)": 7,
    "King Begonias (Begonia rex)": 5,
    "Sky Plant (Tillandsia ionantha)": 14,
}

# Multi-select widget for plant selection
selected_copy = st.multiselect(
    "Select your plants:",
    options=list(default_watering_intervals.keys()),
    default=st.session_state.selected_plants_copy
)

# Update session state with the user's selection
st.session_state.selected_plants_copy = selected_copy

# Watering schedule input for each selected plant with default estimated values
for plant in selected_copy:
    default_value = st.session_state.watering_schedule.get(plant, default_watering_intervals.get(plant, 7))
    watering_days = st.number_input(
        f"How often should {plant} be watered? (Days)",
        min_value=1, max_value=30, value=default_value
    )
    st.session_state.watering_schedule[plant] = watering_days

# Display the selected plants and their watering schedule
if selected_copy:
    st.write("### Your Watering Schedule:")
    for plant in selected_copy:
        st.write(f"🌱 **{plant}**: Every **{st.session_state.watering_schedule[plant]}** days")
else:
    st.write("No plants selected yet.")

# Navigation buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Back"):
        st.switch_page("pages/plant_watering_random.py")  

with col2:
    if st.button("Next"):
        st.switch_page("pages/plant_watering_random_notifications.py")  # Navigate to notification settings
