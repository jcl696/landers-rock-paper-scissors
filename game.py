#game.py
import random

def my_message():
    return "HELLO"

def determine_winner(u, c):
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }

    winning_choice = winners[u][c]

    return winning_choice

# only if this script is executed from the command line should we do all the stuff inside
if __name__ == "__main__":



        #import random 


        #print("Rock, Paper, Scissors, Shoot!")
        #
        #
        ##capture input
        #
        #user_selection = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without quotes):")
        #
        #print ("-----------------")
        #
        #print("User selection:",user_selection)
        #
        #
        ## validate inputs
        #
        #game_options = ["rock", "paper", "scissors"]
        #
        #
        #if user_selection not in game_options:
        #    print("Invalid selection, please run again")
        #    exit()
        #
        #
        #
        ## generate computer selection
        #
        #print("Generating...")
        #
        #
        #
        #computer_selection = random.choice(game_options)
        #
        #print("-----------------")
        #
        #print("Computer selection:", computer_selection)
        #
        #
        ##determine the winner
        #
        ## rock beats scissors, scissors beats paper, paper beats rock
        ## same selections is a tie
        ## can either do conditional logic (if statements) or dictionary
        #
        ###if user_selection == computer_selection:
        # print ("TIE")
        ##elif user_selection == "rock" and computer_selection == "paper":
        ##    print ("PAPER")
        ##elif user_selection == "rock" and computer_selection == "scissors":
        ##    print("ROCK")
        ##elif user_selection == "paper" and computer_selection == "scissors":
        ##    print("SCISSORS")
        ##elif user_selection == "paper" and computer_selection == "rock":
        ##    print("PAPER")
        ##elif user_selection == "scissors" and computer_selection == "paper":
        ##    print("SCISSORS")
        ##elif user_selection == "scissors" and computer_selection == "rock":
        ##    print("ROCK")
        ##
        #

        #display final outputs / outcomes

        # game.py


        print("Rock, Paper, Scissors, Shoot!")  # this is also a comment

        # CAPTURE INPUTS

        user_choice = input(
            "Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")

        print("--------------")
        print("USER CHOICE:", user_choice)

        # VALIDATE INPUTS

        options = ["rock", "paper", "scissors"]

        if user_choice not in options:
            print("INVALID SELECTION, PLEASE TRY AGAIN...")
            exit()

        # GENERATE COMPUTER SELECTION

        computer_choice = random.choice(options)

        print("--------------")
        print("GENERATING...")
        print("COMPUTER CHOICE:", computer_choice)

        # DETERMINE THE WINNER
        #
        # rock beats scissors
        # paper beats rock
        # scissors beats paper
        # same selections is a tie
        #
        # first attribute represents the user, second represents the computer
        winners = {
            "rock": {
                "rock": None,
                "paper": "paper",
                "scissors": "rock",
            },
            "paper": {
                "rock": "paper",
                "paper": None,
                "scissors": "scissors",
            },
            "scissors": {
                "rock": "rock",
                "paper": "scissors",
                "scissors": None,
            },
        }

        winning_choice = winners[user_choice][computer_choice]

        # DISPLAY FINAL OUTPUTS / OUTCOMES

        if winning_choice:
            if winning_choice == user_choice:
                print("YOU WON")
            elif winning_choice == computer_choice:
                print("YOU LOST")
        else:
            print("TIE")

        print("Thanks for playing. Please play again!")
