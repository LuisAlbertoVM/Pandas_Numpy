import numpy as np

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = np.array(lista)
print(type(arr))
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(matriz)
print(matriz)
# los arrays a nivel indexado empiezan desde 0
print(arr[0]+ arr[5])

print(matriz[0,2])

print(arr[1:6])

print(arr[:6])

print(arr[2:])

print(arr[::3])

print(arr[-1])

print(matriz[1:])

print(matriz[1:,0:2])