'''
Ejercicio 5:
Crea un programa llamado InvertirNumero.py que le pida al usuario un número entero y
construya otro en otra variable que sea el original dado la vuelta. Por ejemplo, si el número inicial
es 2356, debe construir el 6532.
'''

num = input("Introduce un numero entero: ")

print(int(num[::-1]))