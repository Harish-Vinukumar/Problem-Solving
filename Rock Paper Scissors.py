"""
A Simple Rock Paper Scissor game
"""
import random

print("***Play Rock-Paper-Scissor with the Computer***")
print("1. Rock\t2. Paper\t3. Scissor")
choice = int(input())

try:
    player_choice = int(choice)
except ValueError:
    print('Enter a valid integer choice!!')

computer_choice = random.randrange(1,4)

if player_choice > 3:
    print('Enter a valid integer choice!!')

if choice == computer_choice:
    print('Draw!!')
elif choice == computer_choice - 1 or choice == computer_choice + 2:
    print('Computer Wins!!')
else:
    print('You Win!!')
