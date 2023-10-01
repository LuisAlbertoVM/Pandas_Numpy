import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books.head(2))

print()
print(df_books.info())

print()
print(df_books.describe())

print()
print(df_books.tail())

print()
print(df_books.memory_usage(deep=True))

print()
print(df_books['Author'].value_counts())

print()
print(df_books.head(1))
print()
df_books = pd.concat([df_books,df_books.head(1)])
print(df_books)

print()
print(df_books.drop_duplicates(keep='last'))

print(df_books.sort_values('Year',ascending=False))