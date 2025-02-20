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

# Initialize session state for selected plants
if 'selected_plants' not in st.session_state:
    st.session_state.selected_plants = []

# Predefined list of common houseplants
plants = [
   "Spider Plant (Chlorophytum comosum)",
   "Aloe Vera (Aloe vera)",
   "Peace Lily (Spathiphyllum spp.)",
   "Snake Plant (Sansevieria spp.)",
   "Pothos (Epipremnum aureum)",
   "Rubber Plant (Ficus elastica)",
   "Swiss Cheese Plant (Monstera deliciosa)",
   "Fiddle Leaf Fig (Ficus lyrata)",
   "ZZ Plant (Zamioculcas zamiifolia)",
   "Jade Plant (Crassula ovata)",
   "English Ivy (Hedera helix)",
   "Philodendron (Philodendron spp.)",
   "Moth Orchid (Phalaenopsis spp.)",
   "Boston Fern (Nephrolepis exaltata)",
   "Parlour Palm (Chamaedorea elegans)",
   "Yucca (Yucca spp.)",
   "African Violet (Saintpaulia spp.)",
   "Chinese Money Plant (Pilea peperomioides)", 
   "Dragon Tree (Dracaena draco)",
   "Weeping Fig (Ficus benjamina)",
   "Prayer Plant (Maranta leuconeura)",
   "String of Pearls (Senecio rowleyanus)",
   "Areca Palm (Dypsis lutescens)",
   "Dumb Cane (Dieffenbachia spp.)",
   "Venus Flytrap (Dionaea muscipula)",
   "Maidenhair Fern (Adiantum spp.)",
   "Poinsettia (Euphorbia pulcherrima)",
   "Amaryllis (Hippeastrum spp.)",
   "Flamingo Flower (Anthurium andraeanum)",
   "Bird's Nest Fern (Asplenium nidus)",
   "Polka Dot Plant (Hypoestes phyllostachya)",
   "Corn Plant (Dracaena fragrans)",
   "Calathea (Calathea spp.)",
   "Heart Leaf Philodendron (Philodendron hederaceum)",
   "Sword Fern (Polystichum munitum)",
   "Cape Jasmine (Gardenia jasminoides)",
   "Tiger Aloe (Aloe variegata)",
   "Velvet Plant (Gynura aurantiaca)",
   "Dwarf Umbrella Tree (Schefflera arboricola)",
   "Flaming Katy (Kalanchoe blossfeldiana)",
   "Zebra Plant (Haworthia fasciata)",
   "Sensitive Plant (Mimosa pudica)",
   "Silver Inch Plant (Tradescantia zebrina)",
   "Living Stones (Lithops spp.)",
   "Pink Quill (Tillandsia cyanea)",
   "Madagascar Jasmine (Stephanotis floribunda)",
   "Joseph's Coat (Codiaeum variegatum)",
   "Cape Primrose (Streptocarpus spp.)",
   "King Begonias (Begonia rex)",
   "Sky Plant (Tillandsia ionantha)"
]

# Multi-select widget for plant selection
selected = st.multiselect(
    "Select your plants:",
    options=plants,
    default=st.session_state.selected_plants
)

# Update session state with the user's selection
st.session_state.selected_plants = selected

# Display the selected plants
if selected:
    st.write("Your selected plants are:", ", ".join(selected))
else:
    st.write("No plants selected yet.")

# Back button with consistent styling
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

if st.button("Back"):
    st.switch_page("pages/plant_care_random.py")  # Return to the previous page