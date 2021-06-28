import pandas as pd



pokedf= pd.read_csv("comics.csv")

print(pokedf.head())

attackdf= pokedf.sort_values(["Attack"], ascending=False)

print(attackdf.head(10))

