import sys
import random

i = 1
number = random.randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

while i < 3:
    if guess == number:
        print("Correct! You win!")
        sys.exit()
    else:
        i +=1
        guess = int(input("Wrong. Guess again: "))
    
print(f"Game over. Correct number was {number}.")