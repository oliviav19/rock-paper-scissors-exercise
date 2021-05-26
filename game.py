# game.py

import random

print("Rock, Paper, Scissors, Shoot!")


user_choice = input("Please choose one of the 'rock', 'paper', 'scissor':")

print("USER CHOICE: ", user_choice)

# validate the input such that only if it is one of the expected values
# ...will we continue with the rest of the program
# ... otherwise we'll stop the program before it tries to do anything else
# ... and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else: 
    print("OOPS, invalid input. Please try again.")
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ", computer_choice)

if(if(user_choice == "rock") and (computer_choice =="rock")) or ((user_choice == "paper") and (computer_choice == "paper")) or ((user_choice == "scissors") and (computer_choice == "scissors"))
print("TIE")

print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")


