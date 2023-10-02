import pandas as pd
import numpy as np

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
 'B': ['B0', 'B1', 'B2', 'B3'],
 'C': ['C0', 'C1', 'C2', 'C3'],
 'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A4', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

print(pd.concat([df1,df2],ignore_index=True))
print(pd.concat([df1,df2],axis=1))

print()
print('Merge')
left_df = pd.DataFrame({'key':['k0','k1','k2','k3'],
 'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3']})

right_df = pd.DataFrame({'key2':['k0','k1','k2','k3'],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3']})
print(left_df)
print(right_df)
print(left_df.merge(right_df, left_on='key',right_on='key2'))

print()
left_df = pd.DataFrame({'key':['k0','k1','k2','k3'],
 'A':['A0','A1','A2','A3'],
 'B':['B0','B1','B2','B3']})

right_df = pd.DataFrame({'key2':['k0','k1','k2',np.nan],
 'C':['C0','C1','C2','C3'],
 'D':['D0','D1','D2','D3']})
print(left_df)
print(right_df)
print(left_df.merge(right_df, left_on='key',right_on='key2',how='left'))

print()
print('Join Match')

left_df = pd.DataFrame({'A':['A0','A1','A2'],
 'B':['B0','B1','B2']},
 index=['k0','k1','k2'])

right_df = pd.DataFrame({'C':['C0','C1','C2'],
 'D':['D0','D1','D2']},
 index=['k0','k1','k2'])
print(left_df.join(right_df))