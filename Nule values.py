import pandas as pd
import numpy as np

dict = {'Col1': [1,2,3,np.nan],
 'Col2': [4,np.nan,6,7],
 'Col3': ['a','b','c',None]}
df = pd.DataFrame(dict)
print(df)
print()
print(df.isnull()*1)
print()
#df = df.fillna('Missing')
#df = df.interpolate()
df = df.dropna()
print(df)