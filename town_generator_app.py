import random
import streamlit as st
import pandas as pd
from PIL import Image

# Lists of possible attributes for towns
town_prefixes = ["Green", "White", "River", "Stone", "Shadow", "Bright", "Silver", "Gold", "Dark", "Iron", "Wind"]
town_suffixes = ["dale", "ton", "ford", "burg", "ville", "haven", "hold", "grove", "stead", "port", "reach"]
economies = ["Farming", "Fishing", "Mining", "Trade", "Craftsmanship", "Logging", "Magic"]
defenses = ["Town Guard", "Wooden Palisade", "Stone Walls", "Militia", "No Defenses", "Magical Barrier"]
population_sizes = ["Small Village (50-100)", "Large Village (100-300)", "Small Town (300-1000)", "Large Town (1000-3000)", "City (3000-10000)", "Metropolis (10000+)"]

# Function to generate a random town name
def generate_town_name():
    prefix = random.choice(town_prefixes)
    suffix = random.choice(town_suffixes)
    return f"{prefix}{suffix}"

# Function to generate a random location name
def generate_location_name():
    prefixes = ["Ancient", "Dark", "Golden", "Silent", "Mystic", "Shadow", "Iron", "Silver", "Hidden", "Sacred"]
    suffixes = ["Tower", "Cavern", "Garden", "Forge", "Tavern", "Library", "Sanctuary", "Guild", "Archives", "Pond"]
    return f"{random.choice(prefixes)} {random.choice(suffixes)}"

# Function to generate a random NPC name
def generate_npc_name():
    first_names = ["Aldric", "Bryn", "Caelan", "Dorian", "Elys", "Faelan", "Garrick", "Hadria", "Iona", "Jareth"]
    titles = ["the Brave", "the Cunning", "the Wise", "the Mysterious", "the Bold", "the Swift", "the Healer", "the Hunter", "the Merchant", "the Sorcerer"]
    return f"{random.choice(first_names)} {random.choice(titles)}"

# Function to generate detailed, random histories for NPCs
def generate_npc_history():
    early_life = [
        "grew up in a small village where they learned the value of hard work and perseverance.",
        "was orphaned at a young age and had to survive on their wits alone, roaming from town to town.",
        "was raised by a family of artisans, learning the intricacies of crafting fine goods.",
        "spent their childhood training under a retired warrior, developing exceptional combat skills.",
        "lived in the wilderness for much of their youth, becoming attuned to nature and its secrets."
    ]
    turning_point = [
        "One day, they encountered a powerful mage who taught them the basics of magic, changing their life forever.",
        "An encounter with bandits left them determined to bring justice to those who prey on the innocent.",
        "They discovered an ancient artifact hidden in the ruins near their home, imbuing them with strange powers.",
        "After witnessing the devastation of a nearby village, they vowed to protect others from such a fate.",
        "A mysterious stranger saved them from a deadly illness, inspiring them to dedicate their life to healing others."
    ]
    career = [
        "They became a renowned adventurer, traveling across distant lands and facing countless dangers.",
        "They joined a secret order dedicated to preserving the balance of magic in the world.",
        "They took up the mantle of a protector, defending their town from external threats and training the local militia.",
        "They became a scholar, using their knowledge to advise leaders and solve ancient mysteries.",
        "They worked as a mercenary, offering their services to those in need, always with a strong moral code."
    ]
    current_role = [
        "Now, they live in the town, using their skills and experience to guide and protect the townspeople.",
        "They have settled down and opened a small shop, but their past adventures are still the talk of the town.",
        "They serve as the town's healer, using their vast knowledge of herbs and magic to cure ailments.",
        "They act as an advisor to the town council, ensuring the town is prepared for any threat that may come.",
        "They spend their days training the next generation, hoping to inspire others to take up the cause of justice."
    ]
    return f"{random.choice(early_life)} {random.choice(turning_point)} {random.choice(career)} {random.choice(current_role)}"

# Function to generate random descriptions for locations
def generate_location_description():
    parts = [
        "This location is known for ",
        "It has been a part of the town for many years, ",
        "The place attracts visitors due to its ",
        "Many believe that ",
        "It stands as a symbol of ",
        "The locals cherish it because ",
        "It is said that ",
        "This spot offers ",
        "It plays an important role in ",
        "The community often gathers here for "
    ]
    continuation = [
        "its historical significance and the unique stories that surround it.",
        "and serves as a key point of interest for travelers and townsfolk alike.",
        "mysterious aura and tales of hidden treasures.",
        "great magic resides within this place, offering protection to the town.",
        "the community, providing a meeting point and cultural hub.",
        "it offers a peaceful retreat from everyday worries.",
        "strange events have occurred here, fueling local legends.",
        "breathtaking views and a sense of mystery.",
        "the town's economy, culture, and traditions.",
        "festivals, storytelling, and other events that foster unity."
    ]
    description = "".join(random.sample(parts, 5)) + " " + "".join(random.sample(continuation, 2))
    return description

# Function to generate detailed, random town history
def generate_town_history(town_name, economy, town_age, annual_festival):
    founding = f"{town_name} was founded {town_age} years ago by a group of settlers seeking a better life. "
    economy_growth = f"The town grew steadily due to its thriving {economy.lower()} industry, attracting people from nearby regions. "
    significant_events = [
        "A devastating flood struck the town fifty years ago, but the resilient townspeople rebuilt it even stronger.",
        "Years ago, the town faced attacks from marauding bandits, but the courageous militia managed to protect everyone.",
        "A great festival was established to celebrate the defeat of a monstrous creature that once threatened the town.",
        "The discovery of rare minerals nearby led to a temporary boom in wealth, bringing new opportunities and challenges.",
        "A legendary hero is said to have lived here, whose bravery inspired the entire community for generations.",
        "The town established trade routes with neighboring regions, boosting economic prosperity and cultural exchange.",
        "A mysterious plague once swept through the town, but thanks to the healer's guild, many lives were saved, and the town survived.",
        "A grand library was built with the help of scholars from distant lands, making the town a center for knowledge and learning.",
        "An old alliance with a nearby dwarven clan brought craftsmanship and expertise, helping to fortify the town against potential threats.",
        "A meteor once struck near the town, and the crater became a place of fascination and mystery, drawing scholars and adventurers alike."
    ]
    community_spirit = "The people of the town are known for their strong sense of community, always ready to help one another in times of need. "
    festival_mention = f"Every year, {town_name} celebrates an annual festival to commemorate its founding and the resilience of its people. " if annual_festival else ""
    return f"{founding}{economy_growth}{random.choice(significant_events)} {random.choice(significant_events)} {community_spirit}{festival_mention}"

# Streamlit UI
st.set_page_config(layout="wide")
st.title("🏰 Fantasy Town Generator")

st.sidebar.header("Town Configuration")
town_name = st.sidebar.text_input("What is the name of your town? (Leave blank for a random name)")
population_size = st.sidebar.selectbox("Select the population size of your town:", population_sizes)
economy = st.sidebar.selectbox("What is the main economy of your town?", economies)
defenses = st.sidebar.selectbox("What type of defenses does your town have?", defenses)
town_age = st.sidebar.number_input("How many years ago was your town founded?", min_value=1, step=1, value=200)
annual_festival = st.sidebar.checkbox("Does your town have an annual festival?")
num_notable_locations = st.sidebar.number_input("How many notable locations should your town have?", min_value=1, step=1, value=10)
num_important_npcs = st.sidebar.number_input("How many important NPCs should your town have?", min_value=1, step=1, value=10)

# File upload input
uploaded_file = st.sidebar.file_uploader("Upload a file to add custom attributes to the town (CSV, DOCX, or images):", type=['csv', 'docx', 'png', 'jpg', 'jpeg'])
if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'csv':
        try:
            if uploaded_file.size > 0:
                try:
                    custom_data = pd.read_csv(uploaded_file, encoding='utf-8', on_bad_lines='skip')
                except pd.errors.ParserError:
                    st.error("The CSV file format is incorrect or contains bad lines. Please check the file format and try again.")
                    custom_data = None
                if custom_data is not None and (custom_data.empty or custom_data.columns.size == 0):
                    st.error("The uploaded CSV file has no columns to parse. Please upload a valid CSV file with data.")
                    custom_data = None
        except UnicodeDecodeError:
            st.error("The file encoding is not supported. Please use a UTF-8 or Latin-1 encoded file.")
            custom_data = None
    elif file_extension == 'docx':
        try:
            from docx import Document
            doc = Document(uploaded_file)
            doc_text = "\n".join([para.text for para in doc.paragraphs])
            st.write("Contents of the uploaded Word file:")
            st.write(doc_text)
        except Exception as e:
            st.error(f"Failed to parse the Word document. Error: {e}")
    elif file_extension in ['png', 'jpg', 'jpeg']:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)
        except Exception as e:
            st.error(f"Failed to display the image. Error: {e}")
    else:
        st.error("Unsupported file type. Please upload a CSV, DOCX, or image file.")

# Generate Town Button
if st.sidebar.button("Generate Town"):
    st.header("✨ Generated Town ✨")
    town = {
        "Name": town_name if town_name else generate_town_name(),
        "Population Size": population_size,
        "Economy": economy,
        "Defenses": defenses,
        "Notable Locations": [
            {
                "Name": generate_location_name(),
                "Description": generate_location_description()  # Ensuring a random and descriptive text for each location
            } for _ in range(num_notable_locations)
        ],
        "Important NPCs": [
            {
                "Name": generate_npc_name(),
                "History": generate_npc_history()
            } for _ in range(num_important_npcs)
        ]
    }
    
    # Description Section
    st.subheader(f"🏛️ Town Overview - {town['Name']}")
    st.markdown(f"**Population Size**: {town['Population Size']}")
    st.markdown(f"**Economy**: {town['Economy']}")
    st.markdown(f"**Defenses**: {town['Defenses']}")
    
    # Town History with Expandable Container
    st.subheader("📜 History")
    with st.expander("Click to see the town history..."):
        history_text = generate_town_history(town['Name'], economy, town_age, annual_festival)
        st.write(history_text)

    # Display Notable Locations as Cards
    st.subheader("🛡️ Notable Locations")
    cols = st.columns(2)
    for idx, location in enumerate(town["Notable Locations"]):
        with cols[idx % 2]:
            st.markdown(f"**📍 {location['Name']}**")
            st.caption(location['Description'])

    # Display Important NPCs as Cards
    st.subheader("👤 Important NPCs")
    npc_cols = st.columns(3)
    for idx, npc in enumerate(town["Important NPCs"]):
        with npc_cols[idx % 3]:
            st.markdown(f"**{npc['Name']}**")
            st.caption(npc['History'])

# Footer or additional information
st.sidebar.write("🛡️ Created for D&D or other fantasy campaigns. Generate unique towns and memorable stories!")
