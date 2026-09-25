import random

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),

    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"
    ),

    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"
    ),

    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"
    ),

    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),

    6: (
        "┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"
    )
}

dice_values_in_current_roll = []

total = 0
number_of_dice = int(input("How many die do you want to roll?: "))

for dice_number in range(number_of_dice):
    dice_value = random.randint(1, 6)
    dice_values_in_current_roll.append(dice_value)

for dice_value in dice_values_in_current_roll:
    total += dice_value

'''
for dice_number in range(number_of_dice):
    for line in dice_art.get(dice_values_in_current_roll[dice_number]):
        print(line)

This displays the dice vertically, which looks kinda ugly ngl.
'''

for line_number in range(5): #whatever the number of strings-used are in the dice. 
    for dice_value in dice_values_in_current_roll:
        print(dice_art.get(dice_value)[line_number], end="")
    print()

print(f"Total: {total}")