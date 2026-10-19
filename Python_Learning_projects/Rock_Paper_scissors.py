import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You won!")
    elif player == "paper" and computer == "rock":
        print("You won!")
    elif player == "scissors" and computer == "paper":
        print("You won!")
    else:
        print("You lose, ha-ha!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")