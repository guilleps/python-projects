import json
import pandas as pd
from sklearn.impute import KNNImputer
import folium
import matplotlib.pyplot as plt
import seaborn as sns

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
print("\n\n",filtered_json_data.head())


# _______________________________________________________________MUESTREO DE ACCIDENTES IN MAP_______________________________________________________________________________________________________________

# mapa = folium.Map(location=[41.8781, -87.6298], zoom_start=10)  # coordenadas de chicagocity

# # Agregar marcadores para cada accidente
# for index, row in filtered_json_data.iterrows():
#     folium.Marker([row['latitude'], row['longitude']]).add_to(mapa)

# # mapa.save('TAREA12_FINAL/data/mapa_accidentes.html')  # almacena los regitros del dataset en un archivo html












# # _______________________________________________________________HISTOGRAMAS Y GRAFICOS_______________________________________________________________________________________________________________



# plt.figure(figsize=(10, 6))
# plt.hist(filtered_json_data['injuries_total'], bins=20, color='skyblue', alpha=0.7)
# plt.xlabel('Total de Lesiones')
# plt.ylabel('Frecuencia')
# plt.title('Distribución de Lesiones Totales')
# plt.show()

# # ------categóricas
# fig, ax = plt.subplots(figsize=(12, 6))
# sns.countplot(x='weather_condition', data=filtered_json_data, palette='viridis', ax=ax)
# ax.set_xlabel('Condición del Tiempo')
# ax.set_ylabel('Conteo')
# ax.set_title('Distribución de Condiciones del Tiempo')
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotar etiquetas del eje x
# plt.tight_layout()  # Ajustar diseño para evitar superposiciones
# plt.show()

# # grafica de dispersión para latitude y longitude
# plt.figure(figsize=(8, 8))
# plt.scatter(filtered_json_data['longitude'], filtered_json_data['latitude'], alpha=0.5, color='green')
# plt.xlabel('Longitud')
# plt.ylabel('Latitud')
# plt.title('Distribución Geoespacial de Accidentes')
# plt.grid(True)
# plt.show()

# # grafica de dispersión para latitude vs. injuries_total
# plt.figure(figsize=(8, 6))
# plt.scatter(filtered_json_data['latitude'], filtered_json_data['injuries_total'], alpha=0.5, color='red')
# plt.xlabel('Latitud')
# plt.ylabel('Total de Lesiones')
# plt.title('Relación entre Latitud y Total de Lesiones')
# plt.grid(True)
# plt.show()


