import numpy as np

arr = np.random.randint(1, 20, 10)
print(arr)
matriz = arr.reshape(2,5)
print(matriz)

print(arr.max())

print(matriz.max(1))
print(arr.argmax())
print(matriz.argmax(0))
