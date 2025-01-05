'''
Crea un programa llamado Porcentajes.py que le pregunte al usuario cuántos chicos y chicas
hay en su clase, y calcule el porcentaje de chicos y chicas. PISTA: para sacar el símbolo del
porcentaje en un texto, debemos duplicarlo %%
'''

chicos = int(input("¿Cuantos chicos hay en clase? "))
chicas = int(input("¿Cuantos chicas hay en clase? "))

clase = chicos + chicas

porcentaje_chicos = ((chicos/clase)*100)
porcentaje_chicas = ((chicas/clase)*100)

print(f'Porcentaje de chicos en la clase:{porcentaje_chicos}% ')
print(f'Porcentaje de chicas en la clase:{porcentaje_chicas}% ')