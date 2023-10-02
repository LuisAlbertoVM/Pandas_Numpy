import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books.head())

print()
print(df_books.pivot_table(index='Author',columns='Genre',values='User Rating'))

print()
print(df_books.pivot_table(index='Genre', columns='Year',values='User Rating',aggfunc='sum'))
