'''
Crea un programa llamado Funciones.py con las siguientes funciones:
1. Una función llamada mcd que reciba dos enteros a y b como parámetros y devuelva el
máximo común divisor de esos parámetros. El máximo común divisor es el número más alto
por el que se pueden dividir los dos números.
2. Una función llamada esPrimo que reciba un número como parámetro y devuelva un
booleano indicando si el número es primo o no
Desde el programa principal, llama a la función mcd para calcular el máximo común divisor de 20
y 12 (debería dar 4), y usa la función esPrimo para sacar los números primos que haya del 1 al 50.
'''

def mcd(a, b):
    if a % b == 0:
        print(f'El MCD es {a / b}')

    if a % b != 0:
        resto = a % b
        if a > b:
            a = resto
            print(f'El MCD es {resto}')
        elif a < b:
            b = resto
            print(f'El MCD es {resto}')

def esPrimo(x):
    for n in range(2, x):
        if x % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

print(f'El máximo común divisor es {mcd(20,12)}')

for i in range(1,51):
    print(f'El numero {i} es primo {esPrimo(i)}')