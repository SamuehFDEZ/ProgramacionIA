import numpy as np
from numpy import dtype

array = np.array([1,2,3,4,5,6,7])
print(array)

array10 = np.array([range(10)])
print(array10)

zeros = np.zeros(3) # array de ceros
print(zeros)

print(zeros.dtype)

zerosEntero = zeros.astype(np.int64) # pasar de float a int32
print(zerosEntero)

print(zerosEntero.dtype)

zeros = np.zeros(4, dtype=np.int32) # crea un array de 4 ceros de tipo int32

print(zeros)

print(array.ndim) # numero de dimensiones

print(array.shape) # fila con 7 numeros

array2 = np.zeros([3,3], dtype=np.int32)

print(array2.shape)



# print([0:2,2:-1])