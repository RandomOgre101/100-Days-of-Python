import random
import os
def clear():
  os.system("cls")
from art import logo, vs
from game_data import data

def check():
    a = selection_A['follower_count']
    b = selection_B['follower_count']
    check.correct_answerA = None
    check.correct_answerB = None
    if a > b:
        check.correct_answerA = True
        check.correct_answerB = False
    elif b > a:
        check.correct_answerA = False
        check.correct_answerB = True

def compare():
    print(logo)
    print(f"\nCompare A: {selection_A['name']}, a {selection_A['description']}, from {selection_A['country']}")
    print(vs)
    print(f"\nAgainst B: {selection_B['name']}, a {selection_B['description']}, from {selection_B['country']}\n")
    check()


score = 0
should_continue = True
selection_A = random.choice(data)
selection_B = random.choice([x for x in data if x not in [selection_A,]])

while should_continue:
    compare()
    if check.correct_answerA:
        if input("\nWho has more followers? Type 'A or 'B: ") == 'A':
            score += 1
            clear()
            print(f"You're right! Current score: {score}")
            selection_A = selection_B
            selection_B = random.choice([x for x in data if x not in [selection_B,]])

        else: 
            should_continue = False
            clear()
            print(logo)
            print(f"\nSorry thats wrong. Final score: {score}\n")

    elif check.correct_answerB:
        if input("\nWho has more followers? Type 'A or 'B: ") == 'B':
            score += 1
            clear()
            print(f"You're right! Current score: {score}")
            selection_A = selection_B
            selection_B = random.choice([x for x in data if x not in [selection_B,]])

        else: 
            should_continue = False
            clear()
            print(logo)
            print(f"\nSorry thats wrong. Final score: {score}\n")
