# tribez_game.py
import random
from tribez_data import tribes, descendants, attributes, equipment, quests, stories

def generate_character():
    # Step 1: Choose a Tribe
    tribe = random.choice(tribes)
    print(f"Selected Tribe: {tribe}")

    # Step 2: Choose a Descendant
    descendant = random.choice(descendants[tribe])
    print(f"Descendant: {descendant}")

    # Step 3: Generate Attributes
    character_attributes = {attr: random.randint(1, 10) for attr in attributes}
    print("Attributes:")
    for attr, value in character_attributes.items():
        print(f"  {attr}: {value}")

    # Step 4: Assign Equipment
    character_equipment = random.sample(equipment, 3)
    print("Equipment:", character_equipment)

    # Step 5: Assign a Quest
    quest = random.choice(quests)
    print("Quest:", quest)

    # Step 6: Story
    story = stories[tribe]
    print("Background Story:", story)

# Run the character generation
if __name__ == "__main__":
    generate_character()
