#game.py

print("Rock, Paper, Scissors, Shoot!")


#capture input

user_selection = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without quotes):")

print ("-----------------")

print("User selection:",user_selection)


# validate inputs

game_options = ["rock", "paper", "scissor"]


if user_selection in game_options:
    print("Valid")
else:
    print("Invalid selection, please run again")
    exit()


# generate computer selection

print("Generating...")

#determine the winner


#display final outputs / outcomes
