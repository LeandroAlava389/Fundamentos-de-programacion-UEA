# Función para calcular la temperatura promedio de cada ciudad
def calcular_temperatura_promedio(datos):
    
    #Calcula la temperatura promedio de cada ciudad en base a los datos proporcionados.
    
    promedios = {}
    for ciudad, temperaturas in datos.items(): # Recorre cada ciudad y su lista de temperaturas
        promedio = sum(temperaturas) / len(temperaturas)  # Calcula el promedio de la ciudad
        promedios[ciudad] = round(promedio, 2)  # Redondea a 2 decimales
    return promedios

# Datos de ejemplo: 3 ciudades durante 4 semanas (28 días en total)
datos = {
    "Quito": [13, 14, 15, 13, 14, 15, 16, 14, 13, 15, 14, 13, 14, 15, 14, 13, 15, 16, 13, 14, 15, 16, 13, 14, 15, 14, 13, 14],
    "Guayaquil": [25, 26, 27, 26, 25, 26, 28, 27, 25, 26, 27, 28, 26, 25, 27, 26, 28, 27, 25, 26, 27, 28, 26, 25, 27, 26, 28, 27],
    "Cuenca": [11, 12, 13, 12, 11, 12, 13, 11, 12, 13, 12, 12, 12, 13, 12, 11, 13, 12, 11, 12, 13, 12, 11, 12, 13, 12, 11, 13]
}

# Llamada a la función y salida de resultados
promedios_ciudades = calcular_temperatura_promedio(datos)
for ciudad, promedio in promedios_ciudades.items():
    print(f"La temperatura promedio en {ciudad} es de {promedio}°C")
