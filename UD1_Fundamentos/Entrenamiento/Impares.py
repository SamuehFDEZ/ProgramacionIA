'''
Crea un programa llamado Impares.py que pida al usuario un número entero positivo y muestre
por pantalla todos los números impares desde 1 hasta ese número, separados por comas. Si el
número introducido no es un valor numérico entero, o no es positivo, se lo deberá volver a pedir las
veces que sean necesarias antes de hacer el conteo, mostrando el mensaje de error correspondiente
(por ejemplo, Número no válido).
'''

try:
    num = int(input("Introduce un numero entero positivo "))
    for i in range(num +1):
        if i % 2 != 0:
            print(f'{i} ', end=" ")
        elif num < 0:
            num = int(input("Introduce un numero entero positivo "))
except Exception as e:
    print("Numero no valido:", str(e))
