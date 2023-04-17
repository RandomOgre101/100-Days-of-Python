import random
from HangmanMisc import word_list,logo,stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False

print(logo)

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word and guess not in display:
        print(f"You guessed {guess}, thats not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"\nYou Lose Bozo\n\nThe word was {chosen_word}")

    print(f"\n{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("\nYou win!")
    