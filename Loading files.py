import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0, names=['Namesss', 'Authorrrr', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'])
print(df_books)

print()
print(df_books.columns)