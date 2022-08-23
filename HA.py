import random
def game():
    player_score = 0
    computer_score = 0

    choice = random.randint(1,3)
    print("Der Roboter ist fertig")
    choice = str(choice)
    playerChoice = input("Stein = 1,Papier = 2,Schere = 3/Wahl:")
    if playerChoice == "1" or playerChoice == "2" or playerChoice == "3":
        print("----------------------")
        print("Roboter hat gewählt: " + str(choice))
        if choice == playerChoice:
            print("unentschieden!")
        if choice == "1" and playerChoice == "2":
            player_score += 1
            print("gewonnen!")
            print("player score:" + str(player_score))
            print("computer score:" + str(computer_score))

        if choice == "1" and playerChoice == "3":
            computer_score += 1
            print("verloren")
            print("player score:" + str(player_score))
            print("computer score:" + str(computer_score))
        if choice == "2" and playerChoice == "1":
            computer_score += 1
            print("verloren")
            print("player score:" + str(player_score))
            print("computer score:" + str(computer_score))
        if choice == "3" and playerChoice == "2":
            player_score += 1
            print("gewonnen")
            print("player score:" + str(player_score))
            print("computer score:" + str(computer_score))
        if choice == "2" and playerChoice == "3":
            computer_score += 1
            print("verloren")
            print("player score:" + str(player_score))
            print("computer score:" + str(computer_score))
        if choice == "3"and playerChoice == "1":
            player_score += 1
            print("gewonnen")
            print("player score:" + str(player_score))
            print("computer score:" + str(computer_score))
    else:
        print("Bitte richtig wählen")
        print("Neustart")
        print("----------------------")
        game()





game()
