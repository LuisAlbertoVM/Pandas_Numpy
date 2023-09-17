import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], 'float64')
print(arr)
print(arr.dtype)

arr = np.array([0, 1, 2, 3, 4])
print(arr)
arr = arr.astype(np.bool_)
print(arr)

arr = np.array([0, 1, 2, 3, 4])
print(arr)
arr = arr.astype(np.string_)
print(arr)

arr = np.array(['0', '1', '2', '3', '4'])
print(arr)
arr = arr.astype(np.int8)
print(arr)