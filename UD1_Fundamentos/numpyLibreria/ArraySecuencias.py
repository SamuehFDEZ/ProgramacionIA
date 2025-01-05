'''
Crea un programa en Python llamado ArraySecuencia.py que defina un array unidimensional con
los números del 10 al 50 (inclusive). Muestra en pantalla el resultado final.
'''
import numpy as np

secuencia = np.linspace(10, 50).astype(np.int32)

print(secuencia)