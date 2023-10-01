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

