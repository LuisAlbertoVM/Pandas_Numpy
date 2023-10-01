import numpy as np

arr = np.arange(0,11)
print(arr)

print()
piece_of_arr = arr[0:6]
print(piece_of_arr)

print()
piece_of_arr[:] = 0
print(piece_of_arr)
print(arr)

print()
arr_copy = arr.copy()
print(arr_copy)
arr_copy[:] = 100
print(arr_copy)
print(arr)