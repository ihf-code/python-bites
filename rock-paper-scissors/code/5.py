import random

print("Welcome to Rock, Paper, Scissors")

user_choice = input("What is your move? (rock, paper, scissors) ")
computer_choice = random.choice(["rock", "paper", "scissors"])

print("You picked " + user_choice)
print("The computer picked " + computer_choice)

if user_choice == "rock":
    if computer_choice == "scissors":
        print("You Win")
    elif computer_choice == "paper":
        print("You Lose")
    else:
        print("It's a draw")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You Win")
    elif computer_choice == "scissors":
        print("You Lose")
    else:
        print("It's a draw")
else:
    if computer_choice == "paper":
        print("You Win")
    elif computer_choice == "rock":
        print("You Lose")
    else:
        print("It's a draw")
