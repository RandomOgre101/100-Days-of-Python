import random
from art import logo


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_hand = []
    player_hand = []
    player_sum = 0
    dealer_sum = 0
    should_continue = True

    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        player_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
        for card in player_hand:
                player_sum += card
        print(f"\nYour cards: {player_hand}, current score: {player_sum}")

        dealer_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
        print(f"\nComputer's first card: {dealer_hand[0]}")

    while should_continue:
        if input("\nType 'y to get another card, type 'n' to pass: ") == "y":
            player_hand.append(random.choice(cards))
            dealer_hand.append(random.choice(cards))

            player_sum = 0
            for card in player_hand:
                player_sum += card

            dealer_sum = 0
            for card in dealer_hand:
                dealer_sum += card

            if player_sum > 21:
                print("\nYou went bust, you lose!")
                print(f"\nYour cards: {player_hand}, final score: {player_sum}")
                print(f"\nComputer's cards: {dealer_hand}, final score: {dealer_sum}")
                should_continue = False

            else:
                print(f"\nYour cards: {player_hand}, current score: {player_sum}")
            
        else:
            player_sum = 0
            for card in player_hand:
                player_sum += card

            dealer_sum = 0
            for card in dealer_hand:
                dealer_sum += card

            should_continue = False

            if player_sum > dealer_sum:
                print("****************************************")
                print("\n\nYou win!")
                print(f"\nYour cards: {player_hand}, final score: {player_sum}")
                print(f"\nComputer's cards: {dealer_hand}, final score: {dealer_sum}")
            
            elif player_sum < dealer_sum and dealer_sum < 22:
                print("****************************************")
                print("\n\nYou lose!")
                print(f"\nYour cards: {player_hand}, final score: {player_sum}")
                print(f"\nComputer's cards: {dealer_hand}, final score: {dealer_sum}")

            elif player_sum < dealer_sum and dealer_sum > 21:
                print("****************************************")
                print("\n\nYou win, Dealer went bust!")
                print(f"\nYour cards: {player_hand}, final score: {player_sum}")
                print(f"\nComputer's cards: {dealer_hand}, final score: {dealer_sum}")

            elif player_sum == dealer_sum:
                print("****************************************")
                print("\n\nIt's a draw.")
                print(f"\nYour cards: {player_hand}, final score: {player_sum}")
                print(f"\nComputer's cards: {dealer_hand}, final score: {dealer_sum}")

blackjack()

