import numpy as np

scalar = np.array(42)
print(scalar)
print(f'El número de dimensiones de un escalar es: {scalar.ndim}')

vector = np.array([1, 2, 3])
print(vector)
print(f'El número de dimensiones de un vector es: {vector.ndim}')

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
print(f'El número de dimensiones de una matriz es: {matriz.ndim}')