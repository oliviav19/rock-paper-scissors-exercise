# game.py

import random
import os 
import dotenv

dotenv.load_dotenv()

PLAYER_NAME = os.getenv("PLAYER_NAME")
print(PLAYER_NAME)

#print("rock, paper, scissors, shoot!")
#print("Welcome,", PLAYER_NAME, "to rock, paper, scissors, shoot!")
print ("-----------------------")
print("Welcome, "+ PLAYER_NAME + " to rock, paper, scissors, shoot!")

print ("-----------------------")
user_choice = input("Please choose one: 'rock', 'paper', 'scissors':")

print ("-----------------------")
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
print ("-----------------------")
#USER WINNING AND TIE SCENARIOS

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "scissors") and (computer_choice == "paper"):
    print("scissors cuts paper, you win!")
elif (user_choice == "rock") and (computer_choice == "scissors"):
    print("rock smashes scissors, you win!")
elif (user_choice == "paper") and (computer_choice == "rock"):
    print("paper covers rock, you win!")

#COMPUTER WINNING SCENARIOS

elif (user_choice == "scissors") and (computer_choice == "rock"):
    print("rock smashes scissors, you lose!")
elif (user_choice == "rock") and (computer_choice == "paper"):
    print("paper covers rock, you lose!")
elif (user_choice == "paper") and (computer_choice == "scissors"):
    print("scissors cuts paper, you lose!")

print ("-----------------------")
print("THIS IS THE END OF OUR GAME. THANKS FOR PLAYING. PLEASE PLAY AGAIN!")


