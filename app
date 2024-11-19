import random
import tkinter as tk
from tkinter import messagebox, simpledialog

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

# Function to display NPC details
def display_npc(npc):
    details = ""
    for key, value in npc.items():
        if isinstance(value, dict):
            details += f"{key}:\n"
            for sub_key, sub_value in value.items():
                details += f"  {sub_key}: {sub_value}\n"
        else:
            details += f"{key}: {value}\n"
    messagebox.showinfo("Generated NPC", details)

# Main Application GUI using Tkinter
def main():
    root = tk.Tk()
    root.title("NPC Generator")

    def on_generate():
        try:
            level = simpledialog.askinteger("Input", "Enter Level:", minvalue=1, maxvalue=20)
            if level is not None:
                npc = generate_npc(level)
                display_npc(npc)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid level.")

    generate_button = tk.Button(root, text="Generate NPC", command=on_generate)
    generate_button.pack(pady=20)

    root.geometry("300x150")
    root.mainloop()

if __name__ == "__main__":
    main()
