"""
Snake vs. Water: Snake drinks the water, hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water.
Gun vs. Snake: Gun will kill the snake and win.
"""
import random

def game():
    choices = [1, 2, 3]
    computer  = random.choice(choices)
    choicedict = {"snake" : 1,
                "water" : 2,
                "gun" : 3}

    user = input("Choose from the following- snake, water or gun: ")
    userchoice = choicedict.get(user.lower())

    if(userchoice == 1 and computer == 2):
        print("You win - Snake drinks the water")
    elif(userchoice == 1 and computer == 3):
        print("You lose - Gun kills the Snake")
    elif(userchoice == 1 and computer == 1):
        print("Tie")
    elif(userchoice == 2 and computer == 3):
        print("You win - The gun wil drown in water")
    elif(userchoice == 2 and computer == 1):
        print("You lose - Snake drinks the water")
    elif(userchoice == 2 and computer == 2):
        print("Tie")
    elif(userchoice == 3 and computer == 1):
        print("You win- Gun kills the snake")
    elif(userchoice == 3 and computer == 2):
        print("You lose - The gun will drown in the water")
    elif(userchoice == 3 and computer == 3):
        print("Tie")

game()
