import pymongo
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
from math import radians, sin, cos, sqrt, atan2
import folium

conect_to_local = "mongodb://localhost:27017/" #conexión al localhost mongodb compass
cliente = MongoClient(conect_to_local) # se crea un objeto MongoClient
local_db = cliente.local #identifica la bd 'local' existente
collection = local_db.map_red_light # accede a la coleccion perteneciente a la db
cursor = collection.find()
dataset = list(cursor)
mongo_data = pd.DataFrame(dataset)

# print(mongo_data)
# print(mongo_data.head()) # Primeras filas del DataFrame
# print(mongo_data.describe())  # muestra como media, desviación estándar, etc.

# __________________________________________FILTRADO DE COLUMNAS____________________________________________________________________

filtered_data = mongo_data.loc[:, ['latitude', 'longitude', 'intersection', 'first_approach', 'second_approach', 'third_approach']]
print("\n\n",filtered_data.head())
# print("\n\n",filtered_data.describe())
# print("\n\n",filtered_data.info())

filtered_data['latitude'] = pd.to_numeric(filtered_data['latitude'], errors='coerce')
filtered_data['longitude'] = pd.to_numeric(filtered_data['longitude'], errors='coerce')

filtered_data['latitude'] = filtered_data['latitude'].round(4)
filtered_data['longitude'] = filtered_data['longitude'].round(4)

# print("\n\n",filtered_data[['latitude', 'longitude']].info())


replace_dict = {'NB': 'north', 'EB': 'east', 'SB': 'south', 'WB': 'west'}
filtered_data['first_approach'] = filtered_data['first_approach'].replace(replace_dict)
filtered_data['second_approach'] = filtered_data['second_approach'].replace(replace_dict)
filtered_data['third_approach'] = filtered_data['third_approach'].replace(replace_dict)







plt.scatter(filtered_data['longitude'], filtered_data['latitude'])
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Distribución de Semáforos en Chicago')
# plt.show()


colors = {'north': 'red', 'south': 'blue', 'east': 'green', 'west': 'orange'}

for approach, data in filtered_data.groupby('first_approach'):
    plt.scatter(data['longitude'], data['latitude'], label=approach, color=colors[approach]) # type: ignore

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Distribución de Semáforos en Chicago')
plt.legend()

# plt.show()


# ________________________________________Crear un mapa centrado en Chicago________________________________________________________________________________________________


chicago_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)

# Iterar sobre los datos y añadir marcadores para cada intersección
for index, row in filtered_data.iterrows():
    # Obtener la latitud, longitud e intersección
    lat = row['latitude']
    lon = row['longitude']
    intersection = row['intersection']
    
    # Crear un marcador para cada intersección
    marker = folium.Marker([lat, lon], popup=intersection)
    marker.add_to(chicago_map)


# chicago_map.save("TAREA12_FINAL/data/semaphores_map.html")  # Guardar el mapa como archivo HTML chicago_map


# ____________________________________________________________________________________________________________________________________________________


# Limpiar y estructurar los datos: Verifica si hay valores nulos o inconsistentes en el dataset y 
# decide cómo tratarlos. Puedes eliminar filas con datos faltantes si no son significativos o tratar 
# de imputar esos valores si son importantes para tu análisis.

# Codificar las direcciones: Las direcciones de aproximación (NB, EB, SB, WB) podrían ser codificadas 
# en números o categorías (por ejemplo, 1 para Northbound, 2 para Eastbound, etc.) para facilitar análisis posteriores.

# Análisis de relaciones espaciales: Puedes utilizar la latitud y longitud para realizar análisis de 
# proximidad, como calcular la distancia entre diferentes semáforos o identificar grupos de semáforos 
# cercanos entre sí.

# Visualización geoespacial: Utiliza bibliotecas como Matplotlib, Seaborn o herramientas específicas 
# de visualización geográfica como Folium para representar los semáforos en un mapa de Chicago, resaltando 
# las intersecciones con diferentes colores o tamaños según la cantidad de semáforos.

# Agregación de datos: Agrupa los semáforos por intersección y realiza cálculos como contar cuántos 
# semáforos hay en cada intersección o encontrar las intersecciones con más semáforos.

# Análisis de patrones de tráfico: Si tienes datos adicionales sobre tráfico o accidentes en esas 
# intersecciones, podrías combinarlos para identificar patrones o correlaciones entre la ubicación 
# de los semáforos y la congestión del tráfico o incidentes viales.