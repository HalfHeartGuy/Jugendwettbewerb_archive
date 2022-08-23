import random
from random import randint

choices = ["rock", "paper", "scissors"]


def computer_choice():
    computer_choice = random.randint(0,2)
    return computer_choice
def player_choiceFunction():
    counter = 0

    player_choice = input("Your choice:")
    if player_choice == "1" or player_choice == "2" or player_choice == "3":
        counter = 0
        return choices[int(player_choice) - 1]
    else:
        print("invalid")


print("1=Stein,2=Papier,3=Schere")

onoff = True
while onoff:
    print("Anleitung:")

    computer = computer_choice()
    print("The bot has chosen")

    player_choice = player_choiceFunction()









