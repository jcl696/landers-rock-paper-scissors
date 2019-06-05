#game.py
import random 


print("Rock, Paper, Scissors, Shoot!")


#capture input

user_selection = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without quotes):")

print ("-----------------")

print("User selection:",user_selection)


# validate inputs

game_options = ["rock", "paper", "scissors"]


if user_selection not in game_options:
    print("Invalid selection, please run again")
    exit()



# generate computer selection

print("Generating...")



computer_selection = random.choice(game_options)

print("-----------------")

print("Computer selection:", computer_selection)


#determine the winner

# rock beats scissors, scissors beats paper, paper beats rock
# same selections is a tie
# can either do conditional logic (if statements) or dictionary

if user_selection == computer_selection:
    print ("TIE")
elif user_selection == "rock" and computer_selection == "paper":
    print ("PAPER")
elif user_selection == "rock" and computer_selection == "scissors":
    print("ROCK")
elif user_selection == "paper" and computer_selection == "scissors":
    print("SCISSORS")
elif user_selection == "paper" and computer_selection == "rock":
    print("PAPER")
elif user_selection == "scissors" and computer_selection == "paper":
    print("SCISSORS")
elif user_selection == "scissors" and computer_selection == "rock":
    print("ROCK")



#display final outputs / outcomes
