import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)

print(df_books.head(2))

print()
print("Drop Columns")
df_books.drop('Genre', axis=1, inplace = True)
print(df_books.head(2))
df_books = df_books.drop('Year',axis=1)
print()
print(df_books.head(2))

print()
del df_books['Price']
print(df_books)

print()
print('Drop rows')
df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
df_books = df_books.drop(range(0,10), axis=0)
print(df_books.head(2))