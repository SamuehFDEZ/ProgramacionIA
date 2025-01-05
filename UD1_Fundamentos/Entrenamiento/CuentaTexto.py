'''
Crea un programa llamado CuentaTexto.py que le pida al usuario un texto, y luego le diga cuántas
veces aparece la palabra Python en ese texto.
'''

texto = input("Dame un texto: ")
numVeces = texto.count('Python')
print(numVeces)