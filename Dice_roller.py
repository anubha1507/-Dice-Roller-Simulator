import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Roller Simulator! 🎲")
while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print(f"You rolled a {result}!")

    choice = input("Do you want to roll again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing!")
        break
