import pandas as pd
import numpy as np

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
#df_books = df_books.drop(range(0,10), axis=0)
print(df_books.head(2))

print()
print('Add Columns')
df_books.head(2)
df_books['New Column'] = np.nan
print(df_books.shape[0])

print()
data = np.arange(0, df_books.shape[0])
df_books['Range'] = data
print(df_books)