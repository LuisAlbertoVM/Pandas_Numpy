import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books)