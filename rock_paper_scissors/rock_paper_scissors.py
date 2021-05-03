choice = input('rock, paper, or scissors? ')
# print(f'You picked: {choice}')

import random
computerChoices = ["rock", "paper", "scissors"]
computerChoice = random.choice(computerChoices)
# print(random.choices(computerChoices))

print(f"User chose {choice} and the computer chose {computerChoice}.")

if choice == computerChoice:
    print(f"TIEEE!!!")
elif choice == "rock":
    if computerChoice == "scissors":
        print("You Win!!")
    else:
        print("You Lose...")
elif choice == "paper":
    if computerChoice == "rock":
        print("You Win!!")
    else:
        print("You Lose...")
elif choice == "scissors":
    if computerChoice == "paper":
        print("You Win!!")
    else:
        print("You Lose...")