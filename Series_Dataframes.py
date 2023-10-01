import pandas as pd

psg_players = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'], 
          index=[1,7,10, 39])
print(psg_players)

print()
psg_players = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messi'])
print(psg_players)

print()
dict = {1: 'Navas', 7: 'Mbappe', 10: 'neymar', 30: 'Messi'}
print(pd.Series(dict))

print()
print(psg_players[0:3])

print()
dict = {'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messo'],
 'Altura': [183, 170, 170, 165.0],
 'Goles': [2, 200, 200, 200]}
df_players = pd.DataFrame(dict, index=[1, 7, 10, 30])
print(df_players)
print(df_players.columns)
print(df_players.index)