import random

print("Welcome to Rock, Paper, Scissors")

user_choice = input("What is your move? (rock, paper, scissors) ")
computer_choice = random.choice(["rock", "paper", "scissors"])

print("You picked " + user_choice)
print("The computer picked " + computer_choice)

if user_choice == "rock":
    print("You picked rock")
elif user_choice == "paper":
    print("You picked paper")
else:
    print("You picked scissors")
