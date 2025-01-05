'''
Crea un programa llamado Media.py que le pida al usuario 4 números enteros y calcule su media
(real). La media debe mostrarse en pantalla con 3 cifras decimales.
'''

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))
numero4 = int(input("Numero 4: "))

media = (numero1 + numero2 + numero3 + numero4) / 4

print(f'La media es {media:.3f}')