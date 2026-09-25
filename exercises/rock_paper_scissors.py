import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    #print(computer)
    while player not in options:
        player =  str(input("Enter a choice. (rock, paper, scissors): "))

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie!")
    elif player ==  "rock" and computer == "scissors":
        print("You Win!")
    elif player ==  "paper" and computer == "rock":
        print("You Win!")
    elif player ==  "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("You lose.")

    if not input("Play again? (y/n): ").strip().lower() == "y":
        running = False

print("Thanks for playing.")