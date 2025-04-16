import random

choices = ["rock", "paper", "scissors"]

player_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print(f"Both chose {player_choice}. It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
elif player_choice == "paper" and computer_choice == "rock":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Player wins! {player_choice} beats {computer_choice}.")
else:
    print(f"Computer wins! {computer_choice} beats {player_choice}.")
