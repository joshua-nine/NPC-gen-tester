import random
import streamlit as st

# Lists of possible attributes for NPCs
names = [
    "Arin", "Brielle", "Calvin", "Delphine", "Eldric", "Fiora", "Gareth", "Hilda", "Ivor", "Jasmine",
    "Kira", "Lysander", "Mira", "Nolan", "Oriana", "Percival", "Quinn", "Rhea", "Soren", "Thalia", "Ulric", "Vera", "Wendell", "Xara", "Yorick", "Zara"
]
races = [
    "Human", "Elf", "Dwarf", "Orc", "Halfling", "Tiefling", "Dragonborn", "Gnome", "Aasimar", "Genasi", "Tabaxi", "Kenku"
]
classes = [
    "Fighter", "Wizard", "Rogue", "Cleric", "Ranger", "Bard", "Paladin", "Druid", "Barbarian", "Monk", "Sorcerer", "Warlock",
    "Artificer", "Blood Hunter"
]
personalities = [
    "Friendly", "Suspicious", "Aggressive", "Helpful", "Timid", "Arrogant", "Cunning", "Charming", "Stoic", "Eccentric",
    "Gregarious", "Sarcastic", "Melancholic", "Zealous", "Pessimistic", "Optimistic"
]
motivations = [
    "Seeking revenge", "Protecting family", "Gathering information", "Making money", "Seeking adventure", "Hiding a secret",
    "Serving a deity", "Power hungry", "Protecting a secret", "Escaping a dark past", "Finding lost knowledge", "Proving themselves"
]
quirks = [
    "Always whistles", "Speaks in rhymes", "Forgets names", "Constantly hungry", "Afraid of magic", "Collects shiny objects",
    "Talks to animals", "Never makes eye contact", "Always speaks in a whisper", "Laughs at inappropriate times", "Obsessed with cleanliness"
]
backgrounds = [
    "Noble", "Soldier", "Criminal", "Sage", "Hermit", "Merchant", "Farmer", "Entertainer", "Gladiator", "Spy", "Acolyte", "Guild Artisan"
]
alignments = [
    "Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"
]
abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

# Function to generate ability scores
def generate_ability_scores():
    return {ability: random.randint(3, 18) for ability in abilities}

# Function to generate a random NPC
def generate_npc(level):
    npc = {
        "Name": random.choice(names),
        "Race": random.choice(races),
        "Class": random.choice(classes),
        "Background": random.choice(backgrounds),
        "Alignment": random.choice(alignments),
        "Personality": random.choice(personalities),
        "Motivation": random.choice(motivations),
        "Quirk": random.choice(quirks),
        "Ability Scores": generate_ability_scores(),
        "Level": level
    }
    return npc

# Streamlit UI
st.title("NPC Generator")

num_npcs = st.number_input("How many NPCs would you like to generate?", min_value=1, step=1)
level = st.number_input("Enter Level for NPCs", min_value=1, max_value=20, step=1)

if st.button("Generate NPCs"):
    for i in range(num_npcs):
        npc = generate_npc(level)
        st.subheader(f"NPC {i + 1}")
        for key, value in npc.items():
            if isinstance(value, dict):
                st.write(f"{key}:")
                for sub_key, sub_value in value.items():
                    st.write(f"  {sub_key}: {sub_value}")
            else:
                st.write(f"{key}: {value}")
