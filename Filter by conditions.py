import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books.head(2))

print()
greater_than_2016 = df_books['Year']>2016
print(greater_than_2016)
print(df_books[greater_than_2016])

print()
genre_fiction = df_books['Genre'] == 'Fiction'
print(genre_fiction)

print()
print(df_books[greater_than_2016 & genre_fiction])

print()
print(df_books[~greater_than_2016])