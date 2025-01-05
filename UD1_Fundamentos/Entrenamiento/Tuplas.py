'''
Crea un programa llamado Tuplas.py donde le pidas al usuario que rellene su dirección postal, que
estará formada por su nombre de calle (texto), número de puerta (entero) y número de piso (entero).
Almacena los datos en una tupla y luego muestra por pantalla el resultado (campo a campo).
'''

print("Rellena tu dirección postal")
calle = input("Introduce el nombre de tu calle: ")
puerta = int(input("Introduce el numero de tu puerta: "))
piso = int(input("Introduce el numero de tu piso: "))

tupla = calle, puerta, piso

print(tupla)