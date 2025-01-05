import json
import matplotlib.pyplot as plt

'''
1. Carga del JSON: importa el archivo JSON proporcionado, usando la librería json de 
Python, y carga los datos en un diccionario.
'''

with open('procesar_respuesta_API/textdetections.json5', 'r') as fichero:
    datos = json.load(fichero)
    
print("Claves principales del JSON:")
print(datos.keys())
texto = datos['TextDetections']
print(json.dumps(texto, indent=4))


'''
3. Extracción de textos y confidencias:
•Recorre la lista TextDetections para obtener:
•El texto detectado (DetectedText).
•El nivel de confianza (Confidence).
•El tipo de elemento (Type: LINE o WORD).
•Muestra o almacena los textos junto con su nivel de confianza
'''
print("--------------------------------------------------------")
resultados = []

for palabra in texto:
    texto = palabra.get("DetectedText")
    confianza = palabra.get("Confidence")
    tipo = palabra.get("Type")
    resultados.append({"Texto": texto, "Confianza": confianza, "Tipo": tipo})

for resultado in resultados:
    print(f"Texto: {resultado['Texto']}, Confianza: {resultado['Confianza']}, Tipo: {resultado['Tipo']}")
    

'''
4. Organización y visualización:
•Agrupa las palabras en líneas usando la relación ParentId.
•Ordena las líneas según su posición vertical (Top de BoundingBox).
•Muestra las líneas de texto completas en el orden correcto.
Ejemplo de salida esperada: 
Línea 1: IT'S (Confianza: 99.35%)
Línea 2: MONDAY (Confianza: 99.62%)
Línea 3: but keep (Confianza promedio: 99.59%)
Línea 4: Smiling (Confianza: 88.95%)

Texto completo detectado:
"IT'S MONDAY but keep Smiling"
'''

print("------------------------------------------------------------")

texto2 = datos['TextDetections']
lineas = {}

for item in texto2:
    if item.get("Type") == "LINE":  
        parent_id = item["Id"]
        lineas[parent_id] = {
            "Texto": item["DetectedText"],
            "Confianza": item["Confidence"],
            "Top": item.get("Geometry", {}).get("BoundingBox", {}).get("Top", 0),
        }

lineas_ordenadas = sorted(lineas.values(), key=lambda x: x["Top"])

print("Lineas de texto detectadas:")
for i, linea in enumerate(lineas_ordenadas, start=1):
    print(f"Linea {i}: {linea['Texto']} (Confianza: {linea['Confianza']:.2f}%)")

texto_completo = " ".join([linea["Texto"] for linea in lineas_ordenadas])
print("\nTexto completo detectado:")
print(f'"{texto_completo}"')