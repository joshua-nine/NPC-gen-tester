import random
import streamlit as st

# List of syllables for generating random names
syllables = [
    "a", "be", "ca", "da", "el", "fa", "gar", "hel", "in", "jor", "ka", "la", "mi", "na", "or", "pa", "qui", "ra", "sa", "ta", "ul", "va", "wen", "xen", "yra", "zar"
]

# Function to generate a random name
def generate_random_name():
    name_length = random.randint(2, 4)  # Random name length between 2 and 4 syllables
    name = "".join(random.choice(syllables) for _ in range(name_length))
    return name.capitalize()

# Function to generate ability scores
def generate_ability_scores():
    return {ability: random.randint(3, 18) for ability in abilities}

import random
import streamlit as st

# Lists for NPC Attributes
races = [
    "Human", "Elf (High Elf)", "Elf (Wood Elf)", "Elf (Drow)", "Dwarf (Hill Dwarf)", "Dwarf (Mountain Dwarf)",
    "Halfling (Lightfoot)", "Halfling (Stout)", "Dragonborn", "Tiefling", "Gnome (Forest Gnome)", "Gnome (Rock Gnome)",
    "Half-Orc", "Half-Elf", "Aasimar", "Firbolg", "Goliath", "Genasi (Air)", "Genasi (Earth)", "Genasi (Fire)", "Genasi (Water)",
    "Kenku", "Tabaxi", "Lizardfolk", "Triton", "Bugbear", "Hobgoblin", "Kobold", "Yuan-ti Pureblood",
    "Gith (Githyanki)", "Gith (Githzerai)", "Warforged", "Changeling", "Kalashtar", "Shifter (Beasthide)", "Shifter (Longtooth)",
    "Shifter (Swiftstride)", "Shifter (Wildhunt)", "Vedalken", "Simic Hybrid", "Loxodon", "Centaur", "Leonin",
    "Satyr", "Fairy", "Harengon", "Eladrin", "Shadar-kai", "Duergar", "Orc of Exandria"
]
classes = ["Fighter", "Wizard", "Rogue", "Cleric", "Ranger", "Bard", "Paladin", "Druid", "Barbarian", "Monk", "Sorcerer", "Warlock", "Artificer", "Blood Hunter"]
backgrounds = ["Noble", "Soldier", "Criminal", "Sage", "Hermit", "Merchant", "Farmer", "Entertainer", "Gladiator", "Spy", "Acolyte", "Guild Artisan"]
alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]
abilities = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
skills = [
    "Acrobatics (Dex)", "Animal Handling (Wis)", "Arcana (Int)", "Athletics (Str)", "Deception (Cha)",
    "History (Int)", "Insight (Wis)", "Intimidation (Cha)", "Investigation (Int)", "Medicine (Wis)",
    "Nature (Int)", "Perception (Wis)", "Performance (Cha)", "Persuasion (Cha)", "Religion (Int)",
    "Sleight of Hand (Dex)", "Stealth (Dex)", "Survival (Wis)"
]

# Ability abbreviation to full name mapping
ability_map = {
    "Str": "Strength",
    "Dex": "Dexterity",
    "Con": "Constitution",
    "Int": "Intelligence",
    "Wis": "Wisdom",
    "Cha": "Charisma"
}

# Function to generate ability scores using 4d6 drop the lowest
def generate_ability_scores():
    ability_scores = {}
    for ability in abilities:
        rolls = sorted([random.randint(1, 6) for _ in range(4)], reverse=True)  # Roll 4d6 and drop the lowest
        score = sum(rolls[:3])  # Take the highest 3 rolls
        ability_scores[ability] = {"Score": score, "Rolls": rolls}  # Store both the final score and the rolls used
    return ability_scores

# Function to generate skills scores based on abilities
def generate_skill_scores(ability_scores):
    skill_scores = {}
    for skill in skills:
        ability_abbr = skill.split(" ")[-1].strip("()")
        ability_full = ability_map[ability_abbr]
        skill_scores[skill] = ability_scores[ability_full]["Score"] + random.randint(0, 2)  # Add slight variation
    return skill_scores

# Hit Die Mapping by Class
hit_die_map = {
    "Barbarian": 12, "Fighter": 10, "Paladin": 10, "Ranger": 10, "Bard": 8, "Cleric": 8, "Druid": 8,
    "Monk": 8, "Rogue": 8, "Warlock": 8, "Sorcerer": 6, "Wizard": 6, "Artificer": 8, "Blood Hunter": 10
}

# Function to generate a random NPC
def generate_npc(level):
    ability_scores = generate_ability_scores()
    skill_scores = generate_skill_scores(ability_scores)
    
    npc_class = random.choice(classes)
    hit_die = hit_die_map.get(npc_class, 8)  # Default to d8 if not found

    # Generate hit points by rolling hit die for each level (for simplicity, adding level times CON modifier)
    constitution_modifier = (ability_scores["Constitution"]["Score"] - 10) // 2
    hit_points = hit_die + sum(random.randint(1, hit_die) for _ in range(level - 1)) + level * constitution_modifier
    
    npc = {
        "Name": generate_random_name(),
        "Race": random.choice(races),
        "Class": npc_class,
        "Background": random.choice(backgrounds),
        "Alignment": random.choice(alignments),
        "Ability Scores": ability_scores,
        "Skill Scores": skill_scores,
        "Level": level,
        "Hit Points": {"Total": hit_points, "Hit Die": f"{level}d{hit_die} + {level * constitution_modifier}"},
        "Speed": random.choice([25, 30, 35]),
        "Armor Class": random.randint(10, 18),
        "Proficiency Bonus": 2 + (level - 1) // 4,
    }
    return npc

# Function to generate a random name using syllables
def generate_random_name():
    syllables = ["a", "be", "ca", "da", "el", "fa", "gar", "hel", "in", "jor", "ka", "la", "mi", "na", "or", "pa", "qui", "ra", "sa", "ta", "ul", "va", "wen", "xen", "yra", "zar"]
    name_length = random.randint(2, 4)  # Random name length between 2 and 4 syllables
    name = "".join(random.choice(syllables) for _ in range(name_length))
    return name.capitalize()

# Streamlit UI
st.title("🧙 D&D NPC Character Sheet Generator")

# Sidebar configuration
st.sidebar.header("NPC Settings")
num_npcs = st.sidebar.number_input("How many NPCs would you like to generate?", min_value=1, step=1)
level = st.sidebar.number_input("Enter Level for NPCs", min_value=1, max_value=20, step=1)

if st.sidebar.button("Generate NPCs"):
    st.header("Generated NPCs")
    for i in range(num_npcs):
        npc = generate_npc(level)
        with st.expander(f"NPC {i + 1}: {npc['Name']} ({npc['Class']})", expanded=False):
            # Character Details in Columns
            st.subheader("General Information")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**Name**: {npc['Name']}")
                st.markdown(f"**Race**: {npc['Race']}")
                st.markdown(f"**Class**: {npc['Class']}")
                st.markdown(f"**Background**: {npc['Background']}")
                st.markdown(f"**Alignment**: {npc['Alignment']}")
            with col2:
                st.markdown(f"**Level**: {npc['Level']}")
                st.markdown(f"**Hit Points**: {npc['Hit Points']['Total']} ({npc['Hit Points']['Hit Die']})")
                st.markdown(f"**Armor Class**: {npc['Armor Class']}")
                st.markdown(f"**Speed**: {npc['Speed']} ft")
                st.markdown(f"**Proficiency Bonus**: +{npc['Proficiency Bonus']}")

            # Display Ability Scores
            st.subheader("Ability Scores")
            ability_cols = st.columns(3)
            for idx, (ability, details) in enumerate(npc["Ability Scores"].items()):
                with ability_cols[idx % 3]:
                    st.markdown(f"**{ability}**: {details['Score']} (Rolls: {details['Rolls']})")

            # Display Skill Scores
            st.subheader("Skills")
            skill_cols = st.columns(3)
            for idx, (skill, score) in enumerate(npc["Skill Scores"].items()):
                with skill_cols[idx % 3]:
                    st.markdown(f"**{skill}**: {score}")

# Footer or additional information
st.sidebar.write("🛡️ Created for fun D&D campaigns. Generate NPCs with their character sheets!")
