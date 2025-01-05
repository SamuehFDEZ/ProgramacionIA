'''
Crea un programa llamado MatrizSecuencia.py que defina una matriz de 3 filas y 3 columnas con
los números del 0 al 8. Imprime el resultado por pantalla.
'''

import numpy as np

array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
array2 = np.reshape(array1, (3, 3))

print(array2)
# También array2 = array1.reshape((2, 4))
# array2 = [[1 2 3 4][5 6 7 8]] (2 filas, 4 columnas)