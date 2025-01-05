'''
Crea un programa llamado BuscaNumeros.py que le pida al usuario que escriba números. El
programa los irá añadiendo uno tras otro a una lista hasta que el usuario escriba 0. Entonces, le
pedirá que diga un número y le indicará en qué posiciones de la lista aparece ese número.
'''


numeros = []

# Recoger números del usuario
while True:
    numero = int(input("Escribe un número (0 para terminar): "))
    if numero == 0:
        break
    numeros.append(numero)

# Buscar número en la lista
buscar = int(input("Escribe el número que quieres buscar: "))
posiciones = [i for i, x in enumerate(numeros) if x == buscar]

# Mostrar resultados
if posiciones:
    print(f"El número {buscar} aparece en las posiciones: {posiciones}")
else:
    print(f"El número {buscar} no se encuentra en la lista.")
