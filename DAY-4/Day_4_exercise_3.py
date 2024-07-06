# Rock, Paper and Scisors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

#User Choice
user_choice = int(input("What do you Choose ? Type 0 for ROCK, 1 for PAPER and 2 for SCISSORS:\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed a invalida number, you lose!")
else:
    print("User Choice:\n",game_images[user_choice])

#Computer Choice:

    computer_choice = random.randint(0,2)
    print("Computer Choice:\n",game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!!")

    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!!")

    elif user_choice > computer_choice:
        print("You Win!!")

    elif computer_choice > user_choice:
        print("You Lose!!")

    elif computer_choice == user_choice:
        print("It's a Drawn!!")
        
'''
How to fix the IndexError:
The IndexError likely occurs when the user enters a number that is not 0, 1, or 2. This causes game_images[user_choice] to try to access an index that does not exist in the game_images list.

You can fix this by adding a check to ensure that user_choice is within the valid range before attempting to print the user's choice. Here’s the modified code:
'''