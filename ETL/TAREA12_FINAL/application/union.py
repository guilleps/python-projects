from pymongo import MongoClient
import pandas as pd
import requests


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

filtered_data = mongo_data.loc[:, ['latitude', 'longitude', 'intersection']]
# print("\n\n",filtered_data.head())
# print("\n\n",filtered_data.describe())
# print("\n\n",filtered_data.info())

filtered_data['latitude'] = pd.to_numeric(filtered_data['latitude'], errors='coerce')
filtered_data['longitude'] = pd.to_numeric(filtered_data['longitude'], errors='coerce')

filtered_data['latitude'] = filtered_data['latitude'].round(4)
filtered_data['longitude'] = filtered_data['longitude'].round(4)

# print("\n\n",filtered_data[['latitude', 'longitude']].info())


# replace_dict = {'NB': 'north', 'EB': 'east', 'SB': 'south', 'WB': 'west'}
# filtered_data['first_approach'] = filtered_data['first_approach'].replace(replace_dict)
# filtered_data['second_approach'] = filtered_data['second_approach'].replace(replace_dict)
# filtered_data['third_approach'] = filtered_data['third_approach'].replace(replace_dict)

print("\n\n",filtered_data)

# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________



import pandas as pd

data_traffic = pd.read_csv('TAREA12_FINAL/data/Chicago_Traffic_Tracker_Congestion_Estimates_by_Regions.csv', delimiter=',')

# print(data_traffic.head())
# print("\n\n",data_traffic.describe())
# print("\n\n",data_traffic.info())
# print("\n\n",data_traffic.isnull().sum())
# print("\n\n",data_traffic.duplicated().sum())

columnas_eliminar = ['CURRENT_SPEED', 'LAST_UPDATED']
data_traffic = data_traffic.drop(columns=columnas_eliminar)
# print("\n\n",data_traffic.head())

data_traffic['REGION'] = data_traffic['REGION'].astype('string')
data_traffic['REGION'] = data_traffic['REGION'].astype('string')


data_traffic = data_traffic.rename(columns={'REGION': 'region', 
                                            'REGION_ID': 'region_id',
                                            'WEST': 'west',
                                            'EAST': 'east',
                                            'SOUTH': 'south',
                                            'NORTH': 'north',
                                            'DESCRIPTION': 'description'})

# print("\n\n",data_traffic.info())
print("\n\n",data_traffic)


# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________


# Agrega una columna para almacenar la región a la que pertenece cada semáforo
filtered_data['region'] = ''

# Recorre cada fila en 'filtered_data' y busca la región correspondiente a sus coordenadas
for i, semaphore_row in filtered_data.iterrows():
    lat = semaphore_row['latitude']
    lon = semaphore_row['longitude']
    
    # Lista para almacenar las regiones encontradas para este semáforo
    found_regions = []
    
    # Busca todas las regiones que contienen estas coordenadas
    for j, region_row in data_traffic.iterrows():
        if (lat >= region_row['south'] and lat <= region_row['north'] and 
            lon >= region_row['west'] and lon <= region_row['east']):
            # Almacena las regiones encontradas
            found_regions.append(region_row['region'])
    
    # Asigna las regiones encontradas al semáforo en una cadena separada por comas
    filtered_data.at[i, 'region'] = ', '.join(found_regions)

# Filtra los semáforos que tienen al menos una región asignada
semaphores_within_regions = filtered_data[filtered_data['region'] != '']

# Muestra los semáforos que están dentro de las regiones de Chicago
print("\n\n",semaphores_within_regions)



# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________


merged_data = pd.merge(data_traffic, semaphores_within_regions, on='region', how='inner')
print("\n\n",merged_data)


# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________


import json
import pandas as pd
from sklearn.impute import KNNImputer

with open('TAREA12_FINAL/data/Traffic_Crashes_Crashes.json', 'r') as archivo:
    datos = json.load(archivo)

data = pd.DataFrame(datos)

# print(data.head())

filtered_json_data = data.loc[:, ['weather_condition', 'lighting_condition', 'first_crash_type', 'latitude', 'longitude', 'prim_contributory_cause', 'sec_contributory_cause',
                                       'injuries_total', 'crash_hour', 'crash_day_of_week', 'crash_month']]


# print("\n\n",filtered_json_data.head())
# print("\n\n", filtered_json_data.describe())
# print("\n\n", filtered_json_data.info())
# print(filtered_json_data.isnull().sum())
# print("\n\n", filtered_json_data.duplicated().sum())

# _______________________________________________________________CONVERSION DE DATOS_______________________________________________________________________________________________________________

filtered_json_data['latitude'] = pd.to_numeric(filtered_json_data['latitude'], errors='coerce')
filtered_json_data['longitude'] = pd.to_numeric(filtered_json_data['longitude'], errors='coerce')

imputer = KNNImputer(n_neighbors=5)  
cols_to_impute = ['latitude', 'longitude']
filtered_json_data[cols_to_impute] = imputer.fit_transform(filtered_json_data[cols_to_impute])

filtered_json_data['latitude'] = filtered_json_data['latitude'].round(4)
filtered_json_data['longitude'] = filtered_json_data['longitude'].round(4)

filtered_json_data['injuries_total'].fillna(0, inplace=True)
filtered_json_data['injuries_total'] = filtered_json_data['injuries_total'].astype(int)
filtered_json_data['crash_hour'] = filtered_json_data['crash_hour'].astype(int)
filtered_json_data['crash_day_of_week'] = filtered_json_data['crash_day_of_week'].astype(int)
filtered_json_data['crash_month'] = filtered_json_data['crash_month'].astype(int)
filtered_json_data['prim_contributory_cause'] = filtered_json_data['prim_contributory_cause'].astype('category')
filtered_json_data['sec_contributory_cause'] = filtered_json_data['sec_contributory_cause'].astype('category')
# Acceder a las categorías únicas
# print(filtered_json_data['prim_contributory_cause'].cat.categories)
# Asignar valores numéricos a las categorías
filtered_json_data['prim_contributory_cause'] = filtered_json_data['prim_contributory_cause'].cat.codes

# print("\n\n",filtered_json_data.info())
print("\n\n",filtered_json_data)


# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________



# Agrega una columna para almacenar la región a la que pertenece cada semáforo
filtered_json_data['region'] = ''

# Recorre cada fila en 'filtered_json_data' y busca la región correspondiente a sus coordenadas
for i, semaphore_row in filtered_json_data.iterrows():
    lat = semaphore_row['latitude']
    lon = semaphore_row['longitude']
    
    # Lista para almacenar las regiones encontradas para este semáforo
    found_regions = []
    
    # Busca todas las regiones que contienen estas coordenadas
    for j, region_row in data_traffic.iterrows():
        if (lat >= region_row['south'] and lat <= region_row['north'] and 
            lon >= region_row['west'] and lon <= region_row['east']):
            # Almacena las regiones encontradas
            found_regions.append(region_row['region'])
    
    # Asigna las regiones encontradas al semáforo en una cadena separada por comas
    filtered_json_data.at[i, 'region'] = ', '.join(found_regions)

# Filtra los semáforos que tienen al menos una región asignada
crashes_with_region = filtered_json_data[filtered_json_data['region'] != '']

# Muestra los semáforos que están dentro de las regiones de Chicago
# print("\n\n",crashes_with_region)


merged_data_centralized = pd.merge(crashes_with_region, merged_data, on='region', how='inner')
# print("\n\n",merged_data_centralized)



# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________
# _______________________________________________________________________________________________________________________________________________________________


import pandas as pd
import requests

if __name__ == '__main__':
    url = 'https://data.cityofchicago.org/resource/gzaz-isa6.json?$query=SELECT%0A%20%20%60person_id%60%2C%0A%20%20%60rd_no%60%2C%0A%20%20%60crash_date%60%2C%0A%20%20%60crash_location%60%2C%0A%20%20%60victim%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60geocoded_column%60%2C%0A%20%20%60%3A%40computed_region_vrxf_vc4k%60%2C%0A%20%20%60%3A%40computed_region_6mkv_f3dw%60%2C%0A%20%20%60%3A%40computed_region_bdys_3d7i%60%2C%0A%20%20%60%3A%40computed_region_43wa_7qmu%60%2C%0A%20%20%60%3A%40computed_region_rpca_8um6%60%0AORDER%20BY%20%60crash_date%60%20DESC%20NULL%20FIRST'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data_endpoint = response.json()  # Convierte la respuesta JSON en un diccionario de Python
        data_fatalities = pd.DataFrame(data_endpoint)
        # print("\n\n",data_fatalities.head())
        # print("\n\n",data_fatalities.describe())
        # print("\n\n",data_fatalities.info())
        # print("\n\n",data_fatalities.isnull())
        # print("\n\n",data_fatalities.duplicated())
        
        columnas_a_eliminar = [':@computed_region_bdys_3d7i', ':@computed_region_43wa_7qmu', ':@computed_region_rpca_8um6',
                               ':@computed_region_vrxf_vc4k', ':@computed_region_6mkv_f3dw', 'geocoded_column',
                               'person_id', 'rd_no']
        data_fatalities.drop(columns=columnas_a_eliminar, inplace=True)
        # print("\n\n",data_fatalities)

        
        data_fatalities['latitude'] = pd.to_numeric(data_fatalities['latitude'], errors='coerce')
        data_fatalities['longitude'] = pd.to_numeric(data_fatalities['longitude'], errors='coerce')

        data_fatalities['victim'] = data_fatalities['victim'].astype('string')
        data_fatalities['crash_location'] = data_fatalities['crash_location'].astype('string')

        data_fatalities['latitude'] = data_fatalities['latitude'].round(4)
        data_fatalities['longitude'] = data_fatalities['longitude'].round(4)

        data_fatalities['crash_date'] = pd.to_datetime(data_fatalities['crash_date'])

        data_fatalities['crash_date'] = data_fatalities['crash_date'].dt.strftime('%Y-%m-%d')


        # print("\n\n",data_fatalities.info())
        print("\n\n",data_fatalities.head())




        # Agrega una columna para almacenar la región a la que pertenece cada semáforo
        data_fatalities['region'] = ''

        # Recorre cada fila en 'data_fatalities' y busca la región correspondiente a sus coordenadas
        for i, semaphore_row in data_fatalities.iterrows():
            lat = semaphore_row['latitude']
            lon = semaphore_row['longitude']
            
            # Lista para almacenar las regiones encontradas para este semáforo
            found_regions = []
            
            # Busca todas las regiones que contienen estas coordenadas
            for j, region_row in data_traffic.iterrows():
                if (lat >= region_row['south'] and lat <= region_row['north'] and 
                    lon >= region_row['west'] and lon <= region_row['east']):
                    # Almacena las regiones encontradas
                    found_regions.append(region_row['region'])
            
            # Asigna las regiones encontradas al semáforo en una cadena separada por comas
            data_fatalities.at[i, 'region'] = ', '.join(found_regions)

        # Filtra los semáforos que tienen al menos una región asignada
        fatalities_with_region = data_fatalities[data_fatalities['region'] != '']

        # Muestra los semáforos que están dentro de las regiones de Chicago
        print("\n\n",fatalities_with_region)


        merged_data_centralized_final = pd.merge(merged_data_centralized, fatalities_with_region, on='region', how='inner')
        # print("\n\n",merged_data_centralized_final)

        # ruta_del_archivo = 'TAREA12_FINAL/data/final/kapoo.csv'  # Reemplaza con la ruta y nombre que desees para el archivo
        
        # merged_data_centralized_final.to_csv(ruta_del_archivo, index=False)



# # _________________________________________________________________________________________________________________________________
# # ________________________________________________FINAL____________________________________________________________________________
# # _________________________________________________________________________________________________________________________________

data_chicago = pd.read_csv('TAREA12_FINAL/data/final/kapoo.csv')

print(data_chicago)
# print(data_chicago.info())
# print(data_chicago.isnull().sum())
# print(data_chicago.duplicated().sum())

data_chicago['latitude_x'] = pd.to_numeric(data_chicago['latitude_x'] , errors='coerce')
data_chicago['longitude_x'] = pd.to_numeric(data_chicago['longitude_x'] , errors='coerce')

data_chicago['latitude_y'] = pd.to_numeric(data_chicago['latitude_y'] , errors='coerce')
data_chicago['longitude_y'] = pd.to_numeric(data_chicago['longitude_y'] , errors='coerce')

data_chicago['weather_condition'] = data_chicago['weather_condition'].astype('string')
data_chicago['lighting_condition'] = data_chicago['lighting_condition'].astype('string')
data_chicago['first_crash_type'] = data_chicago['first_crash_type'].astype('string')
data_chicago['crash_location'] = data_chicago['crash_location'].astype('string')
data_chicago['region'] = data_chicago['region'].astype('string')
data_chicago['description'] = data_chicago['description'].astype('string')
data_chicago['victim'] = data_chicago['victim'].astype('string')


import matplotlib.pyplot as plt

# Gráfico de distribución de lesiones totales
plt.figure(figsize=(8, 6))
plt.hist(data_chicago['injuries_total'], bins=20, color='skyblue')
plt.title('Distribución de Lesiones Totales en Accidentes')
plt.xlabel('Número de Lesiones Totales')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()



import seaborn as sns

# Boxplot de lesiones totales por tipo de accidente
plt.figure(figsize=(10, 6))
sns.boxplot(x='first_crash_type', y='injuries_total', data=data_chicago, palette='Set3')
plt.title('Lesiones Totales por Tipo de Accidente')
plt.xlabel('Tipo de Accidente')
plt.ylabel('Número de Lesiones Totales')
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.show()





data_chicago['crash_date'] = pd.to_datetime(data_chicago['crash_date'])

# Crear una nueva columna 'mes' extrayendo el mes de la fecha del accidente
data_chicago['mes'] = data_chicago['crash_date'].dt.month

# Contar la cantidad de accidentes por mes
accidentes_por_mes = data_chicago.groupby('mes').size()

# Gráfico de Área de cantidad de accidentes por mes
plt.figure(figsize=(10, 6))
accidentes_por_mes.plot(kind='area', color='green', alpha=0.5)
plt.title('Cantidad de Accidentes por Mes (Gráfico de Área)')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Accidentes')
plt.xticks(range(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.grid(True)
plt.show()




import folium
import pandas as pd

# Obtener los límites geoespaciales de Chicago
# Reemplaza estos valores con los límites reales de Chicago
chicago_boundaries = {
    "south": 41.644139,
    "north": 42.0190998,
    "west": -87.84621,
    "east": -87.524436
}

# Crear un mapa centrado en Chicago
chicago_map = folium.Map(location=[(chicago_boundaries["south"] + chicago_boundaries["north"]) / 2,
                                    (chicago_boundaries["west"] + chicago_boundaries["east"]) / 2],
                         zoom_start=10)

# Agregar límites geoespaciales de Chicago al mapa (solo a modo de ejemplo)
folium.Rectangle(bounds=[[chicago_boundaries["south"], chicago_boundaries["west"]],
                          [chicago_boundaries["north"], chicago_boundaries["east"]]],
                 color='blue',
                 fill=True,
                 fill_color='blue',
                 fill_opacity=0.1).add_to(chicago_map)

# DataFrame con coordenadas de regiones (ejemplo)
data_chicago = pd.read_csv('tu_archivo.csv')

# Iterar sobre el DataFrame y agregar marcadores por regiones
for index, row in data_chicago.iterrows():
    folium.Marker(
        location=[row['latitude_x'], row['longitude_x']],  # Coordenadas de latitude_x y longitude_x
        popup=row['REGION'],  # Nombre de la región como información adicional en el marcador
        icon=folium.Icon(color='red')  # Color del marcador
    ).add_to(chicago_map)

# Mostrar el mapa
chicago_map.save('index_niga')







