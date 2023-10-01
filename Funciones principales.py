import numpy as np

arr = np.random.randint(1, 20, 10)
print(arr)
matriz = arr.reshape(2,5)
print(matriz)

print(arr.max())

print(matriz.max(1))
print(arr.argmax())
print(matriz.argmax(0))

print()
print(arr.min())
print(matriz.min())
print(matriz.argmin(0))

print()
print(arr)
print(arr.ptp())

print()
print(matriz)
print(matriz.ptp(0))

print()
print(np.percentile(arr, 50))

print()
print(arr.sort())

print()
print(np.median(arr))

print()
np.median(matriz, 0)

print()
print(np.std(arr) ** 2)

print()
print(np.var(arr))

print()
np.mean(arr)

print()
a = np.array([[1,2], [3,4]])
b = np.array([5,6])
b = np.expand_dims(b,axis=0)

print("Number of dimensions of a",a.ndim)
print("Number of dimensions of b", b.ndim)
print(np.concatenate((a,b),axis=0))

print()
print(np.concatenate((a,b.T),axis=1))