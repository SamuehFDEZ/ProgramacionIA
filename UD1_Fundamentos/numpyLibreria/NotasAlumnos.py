'''
Crea un programa en Python llamado NotasAlumnos.py que le pida al usuario las 4 notas de 3
alumnos diferentes y las almacene en un array NumPy (3 filas, una para cada alumno). Después,
deberá calcular la media de cada alumno y añadir esas medias como una columna al final del array,
mostrando el array resultado
'''

import numpy as np
'''
for i in range(4):
    alumno1 = int(input("Dime 4 notas alumno1 "))
    alumno2 = int(input("Dime 4 notas alumno2 "))
    alumno3 = int(input("Dime 4 notas alumno3 "))
    alumno4 = int(input("Dime 4 notas alumno4 "))
'''

import timeit
n = 1000000
listaPython = list(range(n))
np_array = np.arange(n)
def sum_lista():
 return sum(listaPython)
def sum_np_array():
 return np_array.sum()
time_py = timeit.timeit(sum_lista, number=100)
time_np = timeit.timeit(sum_np_array, number=100)
print(f"Tiempo con lista de Python: {time_py:.5f} segundos")
print(f"Tiempo con array de NumPy: {time_np:.5f} segundos")