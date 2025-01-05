'''
Crea un programa llamado Identidad.py que le pida al usuario un tamaño de tabla N y luego le
deje rellenar los datos de N filas y N columnas de enteros. Al finalizar, le deberá decir si la tabla
que ha rellenado se corresponde o no con una matriz identidad. Una matriz identidad es aquella que
tiene unos en su diagonal principal y ceros en el resto. Por ejemplo (para un tamaño 3 x 3):
1 0 0
0 1 0
0 0 1

'''


def es_matriz_identidad(matriz):
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
    return True

n = int(input("Introduce el tamaño de la tabla N: "))
matriz = []

print("Introduce los datos de la matriz:")
for i in range(n):
    fila = list(map(int, input(f"Fila {i + 1}: ").split()))
    matriz.append(fila)

if es_matriz_identidad(matriz):
    print("La matriz es una matriz identidad.")
else:
    print("La matriz no es una matriz identidad.")
