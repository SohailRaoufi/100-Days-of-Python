import random
from art import logo
#Easy = 10 attempt
#Hard = 5 attempt
#Number 1 - 100
#each time it should tell the user the remaining attempts.
print(logo)

EASY_LVL = 10
HARD_LVL = 5
RANDOM_NUM = random.randint(1 , 100)

print("Welcome To Number Guessing Game.")
print("You Have To Guess a Number Between: 1 - 100")
ask_lvl = input("Please Choose Diffeculity: Easy or Hard? ").lower()

if ask_lvl == "easy":
    for i in range(EASY_LVL , 0 , -1):
        print(f"You have {i} Attempts.")
        guess = int(input("Please Guess The Number: "))
        if guess == RANDOM_NUM:
            print(f"You Won and the number is: {RANDOM_NUM}")
            break
        elif guess > RANDOM_NUM:
            print("Too High")
        else:
            print("Too low")
    else:
        print(f"You are Out of Attempts and number is {RANDOM_NUM}")

elif ask_lvl == "hard":
    for i in range(HARD_LVL , 0 , -1):
        print(f"You have {i} Attempts.")
        guess = int(input("Please Guess The Number: "))
        if guess == RANDOM_NUM:
            print(f"You Won and the number is: {RANDOM_NUM}")
            break
        elif guess > RANDOM_NUM:
            print("Too High")
        else:
            print("Too low")
    else:
        print(f"You are Out of Attempts and number is {RANDOM_NUM}")
