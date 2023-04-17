from art import logo
import os
def clear():
  os.system("cls")


def highest(bidding_record):
    highest = 0
    winner=""
    for bidder in bidding_record:
        amount = bidding_record[bidder]
        if amount > highest:
            highest = amount
            winner = bidder
    print(f"\nThe winner is {winner} with a bid of ${highest}!\n")


print(logo)
bidders = {}
run = True
while(run == True):

    print("\nWelcome to the secret auction program.\n")
    name = input("What is your name?:\n")
    bid = int(input("\nWhat is your bid?: $"))
    bidders[name] = bid
    others = input("\nAre there any other bidders? Type 'yes' or 'no'.\n").lower()

    if others == "yes":
        clear()
    elif others == "no": 
        run = False
        clear()
        highest(bidding_record=bidders)





