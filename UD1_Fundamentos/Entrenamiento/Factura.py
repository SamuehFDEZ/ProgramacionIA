'''
Crea un programa llamado Factura.py que le pida al usuario precios para una factura, hasta que
escriba 0. Entonces, el programa debe mostrar el total de la factura con 2 dígitos decimales.
'''

numeros = int(input("Precios para una factura"))

while numeros != 0:
    print(f'{numeros}2f')
    numeros = int(input("Precios para una factura"))
