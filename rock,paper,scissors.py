import random

choices = ["rock", "paper", "scissor"]

user_wins = 0
computer_wins = 0
ties = 0

while True:
    user = input("Enter Rock, Paper, Scissor (or 'quit' to exit): ").lower()

    if user == "quit":
        print("\nGame Over!")
        print("You won:", user_wins)
        print("Computer won:", computer_wins)
        print("Ties:", ties)
        break

    if user not in choices:
        print("Invalid choice. Please try again.\n")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    # Tie case
    if user == computer:
        print("It's a tie!\n")
        ties += 1

    # Win cases written separately
    elif user == "rock" and computer == "scissor":
        print("You win! Rock beats Scissor\n")
        user_wins += 1

    elif user == "paper" and computer == "rock":
        print("You win! Paper beats Rock\n")
        user_wins += 1

    elif user == "scissor" and computer == "paper":
        print("You win! Scissor beats Paper\n")
        user_wins += 1

    # Lose cases written separately
    elif user == "rock" and computer == "paper":
        print("You lose! Paper beats Rock\n")
        computer_wins += 1

    elif user == "paper" and computer == "scissor":
        print("You lose! Scissor beats Paper\n")
        computer_wins += 1

    elif user == "scissor" and computer == "rock":
        print("You lose! Rock beats Scissor\n")
        computer_wins += 1



#another code
# import random
#
# user = input("Enter Rock, Paper or Scissor: ").lower()
# options = ["rock", "paper", "scissor"]
# computer = random.choice(options)
#
# print("Computer chose:", computer)
#
# if user == computer:
#     print("It's a tie!")
# elif user == "rock" and computer == "scissor":
#     print("You win!")
# elif user == "paper" and computer == "rock":
#     print("You win!")
# elif user == "scissor" and computer == "paper":
#     print("You win!")
# elif user in options:
#     print("You lose!")
# else:
#     print("Invalid input!")

