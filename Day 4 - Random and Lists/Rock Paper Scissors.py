import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpsList = [rock,paper,scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: \n"))

if -1 < choice < 3:
    userChoice = rpsList[choice]


    computer = random.randint(0,2)
    compChoice = rpsList[computer]

    print(f"You chose {userChoice}\n")
    print(f"Computer chose {compChoice}\n")

    if choice and computer == 0:
        print("Its a draw!")
    elif choice == 0 and computer == 1:
        print("Computer Wins!")
    elif choice == 0 and computer == 2:
        print("You Win!")
    elif choice == 1 and computer == 0:
        print("You Win!")
    elif choice == 1 and computer == 1:
        print("Its a draw!")
    elif choice == 1 and computer == 2:
        print("Computer Wins!")
    elif choice == 2 and computer == 0:
        print("Computer Wins!")
    elif choice == 2 and computer == 1:
        print("You Win!")
    elif choice == 2 and computer == 2:
        print("Its a draw!")

else:
    print("Invalid Number! You lose!")

