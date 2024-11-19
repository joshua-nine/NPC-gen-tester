import random

# Lists of possible attributes for NPCs
names = ["Arin", "Brielle", "Calvin", "Delphine", "Eldric", "Fiora", "Gareth", "Hilda", "Ivor", "Jasmine"]
races = ["Human", "Elf", "Dwarf", "Orc", "Halfling", "Tiefling", "Dragonborn", "Gnome"]
classes = ["Warrior", "Mage", "Rogue", "Cleric", "Ranger", "Bard"]
personalities = ["Friendly", "Suspicious", "Aggressive", "Helpful", "Timid", "Arrogant", "Cunning"]
motivations = ["Seeking revenge", "Protecting family", "Gathering information", "Making money", "Seeking adventure", "Hiding a secret"]
quirks = ["Always whistles", "Speaks in rhymes", "Forgets names", "Constantly hungry", "Afraid of magic", "Collects shiny objects"]

# Function to generate a random NPC
def generate_npc():
    npc = {
        "Name": random.choice(names),
        "Race": random.choice(races),
        "Class": random.choice(classes),
        "Personality": random.choice(personalities),
        "Motivation": random.choice(motivations),
        "Quirk": random.choice(quirks)
    }
    return npc

# Generate a specified number of NPCs
def generate_npcs(number=1):
    npcs = []
    for _ in range(number):
        npcs.append(generate_npc())
    return npcs

# Example usage
if __name__ == "__main__":
    num_npcs = int(input("How many NPCs would you like to generate? "))
    generated_npcs = generate_npcs(num_npcs)
    for i, npc in enumerate(generated_npcs, 1):
        print(f"\nNPC {i}:\n")
        for key, value in npc.items():
            print(f"{key}: {value}")
