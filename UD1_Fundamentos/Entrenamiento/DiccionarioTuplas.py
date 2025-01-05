'''
Crea un programa llamado DiccionarioTuplas.py donde le pidas al usuario que rellene direcciones
de 4 usuarios, identificados por su clave que será el DNI. Así, para cada usuario rellenará dicho
DNI, y luego los datos de la dirección como en el ejercicio anterior (nombre de calle, número de
puerta y número de piso). Almacenará los datos en un diccionario (asociando cada DNI con su
dirección) y luego le pedirá al usuario que escriba un DNI y mostrará los datos de su dirección, o el
mensaje “El DNI no se encuentra almacenado” si no existe dicha clave.
'''
direcciones = {}

def pedir_direccion():
    calle = input("Nombre de la calle: ")
    numero_puerta = input("Número de puerta: ")
    numero_piso = input("Número de piso: ")
    return (calle, numero_puerta, numero_piso)

for _ in range(4):
    dni = input("Introduce el DNI del usuario: ")
    direccion = pedir_direccion()
    direcciones[dni] = direccion

dni_buscar = input("Introduce el DNI para buscar la dirección: ")

if dni_buscar in direcciones:
    direccion = direcciones[dni_buscar]
    print(f"Dirección del usuario con DNI {dni_buscar}: Calle {direccion}, Puerta {direccion}, Piso {direccion}")
else:
    print("El DNI no se encuentra almacenado")