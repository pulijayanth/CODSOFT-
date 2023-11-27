import random


def get_choice():
    player_choice=input("enter a choice(rock , paper , scissors):")
    options = ["rock","paper","scissors"]
    computer_choice=random.choice(options)

    choices ={"player": player_choice,"computer":computer_choice}

    return choices

def win(player,computer):
    print("you chose : " + player + "\ncomputer chose : " + computer + "\n")
    if player == computer:
         return "draw!"
    elif player == "rock" and computer == "paper" :
        return "you lost"
    elif player == "rock" and computer == "scissors" :
        return "you won"
    elif player == "paper" and computer == "scissors" :
        return "you lost"
    elif player == "paper" and computer == "rock" :
        return "you won"
    elif player == "scissors" and computer == "rock" :
        return "you lost"
    elif player == "scissors" and computer == "paper" :
        return "you won"
    else :
        return "incorrect input"

def greeting():
    return "wellcome fucker"

print(greeting())
choices= get_choice()
print(choices)
w=win(choices["player"],choices["computer"])
print(w)