# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun.
# The gun beats the snake, the water beats the gun, and the snake beats the water.
# Write a python program to create a Snake Water Gun game in Python using if-else statements.
# Do not create any fancy GUI. Use proper functions to check for win.
# import random first, then computer_choice = random.choice(computer) use it for computer
import random

def get_computer_choice():
    choices = ["Snake", "Water", "Gun"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "Snake":
        if computer_choice == "Water":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "Water":
        if computer_choice == "Gun":
            return "You win!"
        else:
            return "Computer wins!"
    elif user_choice == "Gun":
        if computer_choice == "Snake":
            return "You win!"
        else:
            return "Computer wins!"

print("Welcome to Snake, Water and Gun Game.")
while True:    # allows the game to continue until the user decides to quit by entering a number greater than 2.
    try:
        user_choice = int(input("Select your player: 0 for Snake, 1 for Water, 2 for Gun or any other number to quit the game."))
        if user_choice < 0 or user_choice > 2:
            print("Exiting the game!")
            break
        user_choice = ["Snake" , "Water" , "Gun"][user_choice]
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice} as your Player.")
        if user_choice == computer_choice:
            print(f"Computer also chose {computer_choice} as it's Player.")
        else:
            print(f"Computer chose {computer_choice} as it's player.")
        a = determine_winner(user_choice, computer_choice)
        print(a)
    except ValueError:
        print("Invalid Input. Please try again")




















