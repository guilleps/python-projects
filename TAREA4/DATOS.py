import pandas as pd
import os

# Ejercicio 1
archivos_xls = [f"Aemet2019-01-{str(x).zfill(2)}.xls" for x in range(1, 30)]
lista_dataframes = []

for archivo in archivos_xls:
    data = pd.read_excel(archivo)
    data['source_file'] = archivo  # Agregar una columna con el nombre del archivo
    lista_dataframes.append(data)

dataset = pd.concat(lista_dataframes, ignore_index=True)

# Ejercicio 2
filas, columnas = dataset.shape

# Ejercicio 3
primeras_10_filas = dataset.head(10)

# Ejercicio 4
dataset = dataset.rename(columns={'Estación': 'estacion', 'Provincia': 'provincia', 'Temperatura máxima (ºC)': 'temp_max',
                                  'Temperatura mínima (ºC)': 'temp_min', 'Temperatura media (ºC)': 'temp_med',
                                  'Racha (km/h)': 'viento_racha', 'Velocidad máxima (km/h)': 'viento_vel_max',
                                  'Precipitación 00-24h (mm)': 'prec_dia', 'Precipitación 00-06h (mm)': 'prec_0_6h',
                                  'Precipitación 06-12h (mm)': 'prec_6_12h', 'Precipitación 12-18h (mm)': 'prec_12_18h',
                                  'Precipitación 18-24h (mm)': 'prec_18_24h', 'source_file': 'fecha'})

# Ejercicio 5
columnas_hora = dataset.columns[dataset.columns.str.contains(r'\d{2}:\d{2}$')]
dataset[columnas_hora] = dataset[columnas_hora].apply(lambda x: x.str.extract(r'([\d.]+)').astype(float))

# Ejercicio 6
dataset['fecha'] = dataset['fecha'].str.extract(r'(\d{4}-\d{2}-\d{2})')

# Ejercicio 7
tipos_de_datos = dataset.dtypes

# Ejercicio 8
tipos_de_datos_corregidos = {
    'estacion': 'string',
    'provincia': 'string',
    'temp_max': 'float64',
    'temp_min': 'float64',
    'viento_racha': 'float64',
    'viento_vel_max': 'float64',
    'prec_dia': 'float64',
    'prec_0_6h': 'float64',
    'prec_6_12h': 'float64',
    'prec_12_18h': 'float64',
    'prec_18_24h': 'float64',
    'fecha': 'datetime64[ns]'
}

dataset = dataset.astype(tipos_de_datos_corregidos)

# Ejercicio 9
dataset = dataset.dropna(subset=['temp_max', 'viento_racha'])

# Ejercicio 10
resumen_estadistico = dataset.describe()

# Ejercicio 11
muestras_aleatorias = dataset.sample(5)
columnas_temp = dataset.filter(regex='^temp_', axis=1)

# Ejercicio 12
media_por_provincia = dataset.groupby('provincia').mean()

# Ejercicio 13
top_temp_max = dataset[['provincia', 'estacion', 'fecha', 'temp_max']].nlargest(3, 'temp_max')

# Ejercicio 14
bottom_temp_min = dataset[['provincia', 'estacion', 'fecha', 'temp_min']].nsmallest(3, 'temp_min')

# Ejercicio 15
dataset['temp_diff'] = dataset['temp_max'] - dataset['temp_min']

# Ejercicio 16
max_viento_racha_por_provincia = dataset.groupby('provincia')['viento_racha'].max().reset_index()
max_viento_racha_por_provincia = max_viento_racha_por_provincia.sort_values(by='viento_racha', ascending=False)

# Ejercicio 17
max_viento_vel_medio_por_provincia = dataset.groupby('provincia')['viento_vel_max'].max().reset_index()
max_viento_vel_medio_por_provincia = max_viento_vel_medio_por_provincia.sort_values(by='viento_vel_max', ascending=False)

# Ejercicio 18
media_por_provincia = dataset.groupby('provincia').mean()

# Ejercicio 19
dataset['temp_max_anterior'] = dataset['temp_max'].shift(1)
