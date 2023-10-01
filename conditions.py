import numpy as np
arr = np.linspace(1, 10, 10, dtype='int8')
print(arr)

conditions_index = arr > 5
print(conditions_index)

print()
print(arr[conditions_index & (arr < 9)])

print()
arr[arr>5] = 99
print(arr)