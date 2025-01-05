'''
Crea un programa en Python llamado ArrayCeros.py que defina un array unidimensional de 10
ceros (enteros) en NumPy. Después, cambia el tercer cero por un 1. Muestra en pantalla el resultado
final.
'''

import numpy as np

array = np.zeros(10)

print(array)

array[2] = 1

print(array)