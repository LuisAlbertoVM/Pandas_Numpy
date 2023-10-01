import numpy as np
arr = np.linspace(1, 10, 10, dtype='int8')
print(arr)

conditions_index = arr > 5
print(conditions_index)

print()
print(arr[conditions_index & (arr < 9)])