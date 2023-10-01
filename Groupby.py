import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books.head(2))

print()
print(df_books.groupby('Author').count())

#print()
#print(df_books.groupby('Author').mean())

print()
print(df_books.groupby('Author').min())

print()
print(df_books.groupby('Author').max())

print()
print(df_books.groupby('Author').sum())

print()
print(df_books.groupby('Author').sum().loc['William Davis'])

print()
print(df_books.groupby('Author').sum().reset_index())

print()
print(df_books.groupby('Author').agg(['min','max']))

print()
print(df_books.groupby('Author').agg({'Reviews':['max','max'], 'User Rating':'sum'}))

print()
print(df_books.groupby(['Author', 'Year']).count())