import random
import streamlit as st

# Lists of possible attributes for towns
town_prefixes = ["Green", "White", "River", "Stone", "Shadow", "Bright", "Silver", "Gold", "Dark", "Iron", "Wind"]
town_suffixes = ["dale", "ton", "ford", "burg", "ville", "haven", "hold", "grove", "stead", "port", "reach"]
economies = ["Farming", "Fishing", "Mining", "Trade", "Craftsmanship", "Logging", "Magic"]
defenses = ["Town Guard", "Wooden Palisade", "Stone Walls", "Militia", "No Defenses", "Magical Barrier"]
population_sizes = ["Small Village (50-100)", "Large Village (100-300)", "Small Town (300-1000)", "Large Town (1000-3000)", "City (3000-10000)", "Metropolis (10000+)"]
notable_locations = [
    "Blacksmith", "Tavern", "Market Square", "Temple", "Town Hall", "Watchtower", "Library",
    "Herbalist", "Magic Shop", "Inn", "Stables", "Docks", "Guild Hall", "Bakery", "Butcher", "Armory",
    "Potion Shop", "Barracks", "Graveyard", "Alchemist", "Courthouse", "Warehouse", "Trading Post", "Arena",
    "Fishing Dock", "Barracks", "Stable", "Castle", "Clock Tower", "Greenhouse", "Jewelry Shop", "Carpenter",
    "Tailor", "Mill", "Smithy", "Chapel", "Outfitter", "Cobbler", "Water Well", "Garden", "Orphanage", "Park",
    "Sculpture Garden", "Secret Hideout", "Mine Entrance", "River Crossing", "Marketplace", "Hunter Lodge",
    "Adventurer Guild", "Brewery", "Observatory", "Druid Circle", "Archery Range", "Cathedral", "Town Square",
    "Theater", "Bathhouse", "Tannery", "Distillery", "Public Gallows", "Fountain", "Gatehouse", "Watch House",
    "Bell Tower", "Magic Academy", "Town Archives", "Old Ruins", "Armorer's Forge", "Stonecutter's Yard"
]
important_npcs = [
    "Mayor", "Blacksmith", "Tavern Owner", "Priest", "Merchant", "Guard Captain", "Healer", "Innkeeper", "Guild Leader",
    "Stable Master", "Alchemist", "Baker", "Butcher", "Armorer", "Fisherman", "Jeweler", "Carpenter", "Tailor",
    "Chandler", "Cobbler", "Gardener", "Orphan Keeper", "Sculptor", "Druid", "Hunter", "Brewmaster", "Historian",
    "Archery Instructor", "Playwright", "Distiller", "Watch Captain", "Gatekeeper", "Librarian", "Witch", "Magic Instructor",
    "Thief Leader", "Smuggler", "Miner", "Herbalist", "Knight Commander", "Artisan", "Potion Maker", "Wine Seller",
    "Caravan Leader", "Scholar", "Fortune Teller", "Mystic", "Warden", "Crypt Keeper", "Cemetery Caretaker", "Executioner"
]

# Function to generate a random town name
def generate_town_name():
    prefix = random.choice(town_prefixes)
    suffix = random.choice(town_suffixes)
    return f"{prefix}{suffix}"

# Function to generate short histories for NPCs
def generate_npc_history(npc_name):
    histories = [
        "was once a renowned adventurer before settling down.",
        "has a dark secret that only a few in the town know about.",
        "is known for their generosity and kindness.",
        "is rumored to have connections with a powerful guild.",
        "has lived in the town all their life and knows every secret.",
        "is seeking revenge for a wrong done to their family.",
        "has a mysterious past involving magic and strange artifacts.",
        "is the child of a famous hero, living in their shadow.",
        "is trying to protect the town from an unseen threat.",
        "has a penchant for storytelling, often mixing truth with fiction."
    ]
    return f"{npc_name} {random.choice(histories)}"

# Function to generate the full history of the town
def generate_town_history(town_name, population_size, economy, defenses):
    history_events = [
        f"{town_name} was founded over 200 years ago by a group of settlers looking for a place to establish a {economy.lower()} community.",
        f"The town experienced rapid growth due to its prosperous {economy.lower()} industry, attracting many skilled workers and traders.",
        f"{town_name} faced a major threat 50 years ago when a neighboring kingdom attempted to invade. The {defenses.lower()} helped fend off the attack and protect the town.",
        f"A devastating plague swept through the town about 80 years ago, drastically reducing the population. It was thanks to the efforts of local healers that the town survived.",
        f"The discovery of ancient ruins nearby led to an influx of adventurers and scholars, which boosted the economy and brought more people to settle in {town_name}.",
        f"A mysterious artifact was found in the surrounding area, which is now kept in the town archives. Many believe it holds magical powers, drawing curious travelers.",
        f"{town_name} holds an annual festival celebrating its founding, where the entire community gathers in the town square for feasting and performances.",
        f"Years ago, a famous hero who once saved the region decided to retire in {town_name}, bringing fame and respect to the settlement.",
        f"{town_name} has always been known for its community spirit and resilience, especially during times of hardship, such as the great flood that occurred 30 years ago.",
        f"The construction of the {random.choice(notable_locations).lower()} was a major turning point for {town_name}, establishing it as a central hub for travelers and traders."
    ]
    return "\n".join(history_events)

# Function to generate a random town
def generate_town():
    num_notable = min(len(notable_locations), random.randint(10, 100))
    num_npcs = min(len(important_npcs), random.randint(10, 100))
    
    town = {
        "Name": generate_town_name(),
        "Population Size": random.choice(population_sizes),
        "Economy": random.choice(economies),
        "Defenses": random.choice(defenses),
        "Description": f"{generate_town_name()} is a bustling settlement known for its {random.choice(economies).lower()} industry. It has a population of around {random.choice(population_sizes).split('(')[1].strip(')')} residents. The town's defenses consist of {random.choice(defenses).lower()}. Life in {generate_town_name()} is vibrant, with people engaged in {random.choice(economies).lower()} and everyday life defined by its {random.choice(notable_locations).lower()}.",
        "History": generate_town_history(generate_town_name(), random.choice(population_sizes), random.choice(economies), random.choice(defenses)),
        "Notable Locations": random.sample(notable_locations, k=num_notable),
        "Important NPCs": [
            {
                "Name": random.choice(important_npcs),
                "History": generate_npc_history(random.choice(important_npcs))
            } for _ in range(num_npcs)
        ]
    }
    return town

# Streamlit UI
st.title("🏭 Fantasy Town Generator")

# Questions for user input
town_name = st.text_input("What is the name of your town? (Leave blank for a random name)")
population_size = st.selectbox("Select the population size of your town:", population_sizes)
economy = st.selectbox("What is the main economy of your town?", economies)
defenses = st.selectbox("What type of defenses does your town have?", defenses)
town_age = st.number_input("How many years ago was your town founded?", min_value=1, step=1, value=200)
annual_festival = st.checkbox("Does your town have an annual festival?")
num_notable_locations = st.slider("How many notable locations should your town have?", min_value=10, max_value=100)
num_important_npcs = st.slider("How many important NPCs should your town have?", min_value=10, max_value=100)

if st.button("Generate Town"):
    st.header("Generated Town")
    town = generate_town()
    town["Name"] = town_name if town_name else town["Name"]
    town["Population Size"] = population_size
    town["Economy"] = economy
    town["Defenses"] = defenses
    town["Notable Locations"] = random.sample(notable_locations, k=min(num_notable_locations, len(notable_locations)))
    town["Important NPCs"] = [
        {
            "Name": random.choice(important_npcs),
            "History": generate_npc_history(random.choice(important_npcs))
        } for _ in range(min(num_important_npcs, len(important_npcs)))
    ]
    
    # Add more details to history based on user input
    if annual_festival:
        town["History"] += f"\n{town['Name']} also celebrates an annual festival to commemorate its founding, bringing the community together."
    town["History"] = town["History"].replace("200 years ago", f"{town_age} years ago")
    
    st.markdown(f"**Name**: {town['Name']}")
    st.markdown(f"**Population Size**: {town['Population Size']}")
    st.markdown(f"**Economy**: {town['Economy']}")
    st.markdown(f"**Defenses**: {town['Defenses']}")
    st.markdown(f"**Description**: {town['Description']}")
    st.markdown(f"**History**: {town['History']}")
    
    # Display Notable Locations
    st.subheader("Notable Locations")
    for location in town["Notable Locations"]:
        st.markdown(f"- {location}")
    
    # Display Important NPCs
    st.subheader("Important NPCs")
    for npc in town["Important NPCs"]:
        st.markdown(f"- **{npc['Name']}**: {npc['History']}")

# Footer or additional information
st.sidebar.write("🛡️ Created for D&D or other fantasy campaigns. Generate unique towns with interesting features!")
