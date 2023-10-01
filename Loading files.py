import pandas as pd

df_books = pd.read_csv("bestsellers-with-categories.csv", sep=',', header=0)
print(df_books)

print()
print(df_books.columns)

print()
print(pd.read_json("HPCharactersDataRaw.json", typ = 'Series'))

print()
print(df_books[0:4])
print(df_books[['Name','Author','Year']])

print()
print("Loc")
print(df_books.loc[0:4, ['Name', 'Author']])
print(df_books.loc[0:4, ['Reviews']] * -1)
print(df_books.loc[0:4, ['Author']] == 'JJ Smith')