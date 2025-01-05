'''
Crea un programa llamado SumaSecuencia.py que le pida al usuario una secuencia de números
separados por espacios y calcule la suma total de esos números.
'''

lista = []

while True:
    secuenciaNum = int(input("Introduce una secuencia de números: "))
    if secuenciaNum == 0:
        break
    lista.append(secuenciaNum)

print(f'La suma total es {sum(lista)}')