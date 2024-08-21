"""PROJECT 2  – THE PERFECT GUESS  
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player’s guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number. 
Hint: Use the random module."""

import random

comp = random.randrange(1,100)
n = 0
count = 0

while(n!=comp):
    n = int(input("Enter you number: "))
    if(n == comp):
        count += 1
        print(f"Congratulations you won in {count} guesses")
        break
    elif(n>comp):
        print("Lower number please")
        count +=1
    elif(n<comp):
        print("Higher number please")
        count +=1
    else:
        print("Some error occured")
