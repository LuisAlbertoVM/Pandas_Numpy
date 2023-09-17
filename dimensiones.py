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

tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],[[13, 13, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]]])
print(tensor)
print(f'El número de dimensiones de un tensor es: {tensor.ndim}')

# Agregar o eliminar dimensiones
vector = np.array([1, 2, 3], ndmin=10)
print(vector)
print(f'El número de dimensiones de un vector es: {vector.ndim}')

expand = np.expand_dims(np.array([1, 2, 3]), axis = 0)
print(expand)
print(f'El numero de dimensiones con el expand es: {expand.ndim}')

print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)