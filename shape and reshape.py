import numpy as np

arr = np.random.randint(1, 10, (3,2))

print(arr.shape)
print(arr)

print(arr.reshape(1, 6))
print(arr.reshape(2, 3))
print(np.reshape(arr, (1,6)))
print("")
print(np.reshape(arr, (2,3),'C'))
print("")
print(np.reshape(arr, (2,3),'F'))
print("")
print(np.reshape(arr, (2,3),'A'))