import pandas as pd

df = pd.read_csv("squirrel.csv")

count = df["Primary Fur Color"].value_counts()

data = pd.DataFrame(count)
data.to_csv("new_squirrel.csv")
