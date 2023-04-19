import random
from art import logo
print(logo)

def check():
    global should_continue
    global guess
    global number
    global tries

    if guess > number:
                print("Too high. Try again")
                tries -= 1
                print(f"You have {tries} tries to guess the number.\n")
            
    elif guess < number:
            print("Too low. Try again")
            tries -= 1
            print(f"You have {tries} tries to guess the number.\n")

    elif guess == number:
        print(f"Correct! You win! The number was {number}.\n")                
        should_continue = False 



print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number = random.randint(0, 100)
print(number)

tries = 0
diff = input("\nChoose a difficulty. Type 'hard' or 'easy': ")
should_continue = True

if diff == 'easy':
    tries = 10
    print(f"You have {tries} tries to guess the number.")

    while should_continue:
        if tries > 0:
            guess = int(input("Make a guess: "))
            check()

        else:
            print("You ran out of tries!\n")
            should_continue = False

else:
    tries = 5
    print(f"You have 5 tries to guess the number.")

    while should_continue:
        if tries > 0:
            guess = int(input("Make a guess: "))
            check()

        else:
            print("You ran out of tries!\n")
            should_continue = False



