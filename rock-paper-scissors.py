import random

def rps_game():

    while True:
        player_action = input("Rock, paper, or scissors? Enter your choice (or enter 'quit' to stop playing): ")
        possible_actions = ["rock", "paper", "scissors"]
        computer_action = random.choice(possible_actions)
        print(f'You chose {player_action} and the computer chose {computer_action}.')

        if player_action.lower() == 'quit':
            print("Thanks for playing!")
            break
        elif player_action == computer_action:
            print(f"Both players chose {player_action}. It's a tie!")
        elif player_action.lower() == "rock":
            if computer_action == "scissors":
                print("You win!")
            else:
                print("You lose. Try again!")
        elif player_action.lower() == "scissors":
            if computer_action == "paper":
                print("You win!.")
            else:
                print("You lose. Try again!")
        elif player_action.lower() == "paper":
            if computer_action == "rock":
                print("You win!")
            else:
                print("You lose. Try again!")
        else:
            print("Invalid input. Please select 'rock', 'paper', or 'scissors' or enter 'quit' to stop playing.") 

rps_game()