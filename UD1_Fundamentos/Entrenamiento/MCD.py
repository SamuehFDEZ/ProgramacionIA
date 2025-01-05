'''
Crea un programa llamado MCD.py que le pida al usuario dos números n1 y n2 y utilice el
algoritmo de Euclides para calcular su máximo común divisor (MCD). Este número es el divisor
mayor que tienen en común los dos números. Aplicando el algoritmo de Euclides, se calcula de la
siguiente forma:
1. Dividir el mayor de n1 y n2 entre el menor
2. Si la división es exacta (resto 0), el MCD es el número menor
3. Si no, se sustituye el número mayor por el resto de la división, y se vuelve al paso 1
Por ejemplo, para 20 y 12 haríamos algo así:
• Dividimos 20 / 12. No es exacta, y el resto es 8. Reemplazamos 20 por 8
• Dividimos 12 / 8. No es exacta, y el resto es 4. Reemplazamos 12 por 4
• Dividimos 8 / 4. Es exacta, con lo que el MCD es 4.
'''

n1 = int(input("Introduce n1: "))
n2 = int(input("Introduce n2: "))

if n1 % n2 == 0:
    print(f'El MCD es {n1/n2}')

if n1 % n2 != 0:
    resto = n1 % n2
    if n1 > n2:
        n1 = resto
        print(f'El MCD es {resto}')
    elif n1 < n2:
        n2 = resto
        print(f'El MCD es {resto}')






