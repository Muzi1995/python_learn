import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
player_choice = input(
    "Enter... \n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(player_choice)

if player < 1 or player > 3:
    print("You must enter 1, 2 or 3.")
    sys.exit()

computer_choice = random.choice("123")
computer = int(computer_choice)

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")


if player == 1 and computer == 3:
    1
    print("🎉 You Win!")
elif player == 2 and computer == 1:
    print("🎉 You Win!")
elif player == 3 and computer == 2:
    print("🎉 You Win!")
elif player == computer:
    print("😲 Tie Game!")
else:
    print("🐍 Python Wins!")
