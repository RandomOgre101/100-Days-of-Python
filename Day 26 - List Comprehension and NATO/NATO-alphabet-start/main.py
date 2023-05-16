import pandas as pd


#TODO 1. Create a dictionary in this format:
read = pd.read_csv("nat0.csv")
df = pd.DataFrame(read)
nato = {}

for (index, row) in df.iterrows():
    nato[row.letter] = row.code

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word: ").upper()
user_list = [letter for letter in user_input]

nato_list = [nato[letter] for letter in user_input]
print(nato_list)
