import json
import matplotlib.pyplot as plt
'''
1. Carga y exploración del JSON:
•Cargar el archivo JSON usando la biblioteca json.
•Identificar   las   claves   principales   y   sus   subniveles   (FaceDetails,  Emotions, 
Landmarks, etc.)
'''

with open('UD2_HerramientasIA/procesar_respuesta_API/facedetails.json5') as fichero:
    datos = json.load(fichero)
    
print("Claves principales del JSON:")
print(datos.keys())
faceDetails = datos['FaceDetails']
print(json.dumps(faceDetails, indent=4))

'''
2. Extracción y muestra de información básica:
•Buscar y mostrar la edad estimada (rango bajo y alto).
•Mostrar si la persona lleva gafas y/o gafas de sol (y la confianza asociada).
•Determinar el género detectado y su confianza.
'''
primer_elemento = faceDetails[0]
rangoEdad = primer_elemento.get("AgeRange", )

print(f"Edad estimada: {rangoEdad.get('Low')} - {rangoEdad.get('High')} anyos")

eyeglasses = primer_elemento.get("Eyeglasses", )
sunglasses = primer_elemento.get("Sunglasses", )

print(f"Gafas: {'Si' if eyeglasses['Value'] else 'No'} (Confianza: {eyeglasses['Confidence']:.2f}%)")
print(f"Gafas de sol: {'Si' if sunglasses['Value'] else 'No'} (Confianza: {sunglasses['Confidence']:.2f}%)")

gender = primer_elemento.get("Gender", )
print(f"Genero estimado: {gender['Value']} - (Confianza{gender['Confidence']:.2f}%)")

'''
3. Análisis de Emociones:
•Identificar la emoción con el nivel de confianza más alto, y la de nivel más bajo.
•Calcular y mostrar un gráfico de barras con la distribución de emociones (usando 
matplotlib o seaborn, muestra el máximo de 100).
'''

emotions = primer_elemento.get("Emotions", )

maxEmotion = max(emotions, key=lambda x: x['Confidence'])
minEmotion = min(emotions, key=lambda x: x['Confidence'])

print(f'Emocion mas alta: {maxEmotion['Type']} nivel de confianza: {maxEmotion['Confidence']:.2f} %')
print(f'Emocion mas baja: {minEmotion['Type']} nivel de confianza: {minEmotion['Confidence']:.2f} %')

tiposEmociones = [emotion['Type'] for emotion in emotions]
confianzaEmociones = [emotion['Confidence'] for emotion in emotions]

plt.figure(figsize=(10,6))
plt.bar(tiposEmociones, confianzaEmociones, color='red')
plt.title("Emociones")
plt.xlabel('Confianza')
plt.ylabel('Tipo')
plt.xlim(0, 10)
plt.show()

'''
4. Procesamiento de Puntos de Referencia (Landmarks) [opcional]:
•Extraer   las   coordenadas   de   los   puntos   clave   de   la   cara   (por   ejemplo,   ojos,   boca, 
nariz),   luego,   visualizar   estos   puntos   en   una   gráfica   de   dispersión,   simulando   un 
mapa facial
'''
landmarks = primer_elemento['Landmarks']

x = [posicion["X"] for posicion in landmarks]
y = [posicion["Y"] for posicion in landmarks]
labels = [posicion["Type"] for posicion in landmarks]

plt.figure(figsize=(8, 10))
plt.scatter(x, y, color="blue")

for i, label in enumerate(labels):
    plt.text(x[i], y[i], label, fontsize=8, color="red")

plt.gca().invert_yaxis()

plt.title("Mapa Facial - Puntos Clave")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.grid(True)
plt.show()