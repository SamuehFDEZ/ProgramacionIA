'''
Crea un programa llamado NotasNumPy.py que le pida al usuario una secuencia de notas
numéricas, separadas por espacios. Con ellas deberá:
• Crear un array unidimensional con NumPy
• Ordenar las notas de mayor a menor
• Crear un segundo array con las notas aprobadas
• Calcular la media de las notas aprobadas
'''

import numpy as np

tabla = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(tabla[:]) # [5 6 7 8]
