import numpy as np

lista = [1,2]
print(lista)

print()
print(lista * 2)

print()
arr = np.arange(0,10)
print(arr)

arr2 = arr.copy()
print(arr2)

print("operations")
print(arr)
print(arr * 2)
print(arr + 2)
print()
print("Division by 0")
print(1 / arr)

print()
print(arr ** 2)
print(arr + arr2)
print(arr * arr2)

print()
matriz = arr.reshape(2,5)
print(matriz)
matriz2 = matriz.copy()
print(matriz2)
print(matriz * matriz2)
print(np.matmul(matriz, matriz2.T))
print(matriz @ matriz2.T)