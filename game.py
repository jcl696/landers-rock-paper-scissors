#game.py
import random 
print("Rock, Paper, Scissors, Shoot!")


#capture input

user_selection = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without quotes):")

print ("-----------------")

print("User selection:",user_selection)


# validate inputs

game_options = ["rock", "paper", "scissor"]


if user_selection not in game_options:
    print("Invalid selection, please run again")
    exit()



# generate computer selection

print("Generating...")



computer_selection = random.choice(game_options)

print("-----------------")

print("Computer selection:", computer_selection)
#determine the winner


#display final outputs / outcomes
