import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books.head())

def two_times(value):
    return value*2

print()
df_books['Rating_2'] = df_books['User Rating'].apply(two_times)
print(df_books)

print()
df_books['Rating_2'] = df_books['User Rating'].apply(lambda x : x *3)
print(df_books.head())

print()
df_books['Rating_2'] = df_books.apply(lambda x: x['User Rating'] * 2 if x['Genre'] == 'Fiction' else x['User Rating'], axis=1)
print(df_books.head())
