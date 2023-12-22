import os
import pandas as pd

directorio = 'C:/workspace/Python/TAREA4/csv_tarea4/'
dataframes = []

for archivo in os.listdir(directorio):
    if archivo.endswith(".xls"):

        df = pd.read_excel(os.path.join(directorio, archivo))
        df['AEMET FILENAMES'] = archivo
        dataframes.append(df)

dataset = pd.concat(dataframes, ignore_index=True)


#¿Cuantas filas y columnas contiene el dataset? -- 2
num_filas, num_columnas = dataset.shape
print(f"El dataset tiene: \n{num_filas} filas \n{num_columnas} columnas")


#Muestre las primeras 10 filas del dataset -- 3
print(f'{dataset.head(10)}\n')


#Renombre las columnas para que sea más sencillo usarlas y ocupen menos espacio en pantalla. -- 4
columns = {'Unnamed: 1': 'estacion', 'Unnamed: 2': 'provincia', 'Unnamed: 3': 'temp_max',
           'Unnamed: 4': 'temp_min', 'Unnamed: 5': 'temp_med', 'Unnamed: 6': 'viento_racha',
           'Unnamed: 7': 'viento_vel_max', 'Unnamed: 8': 'prec_dia',
           'Unnamed: 9': 'prec_0_6h', 'Unnamed: 10': 'prec_6_12h',
           'Unnamed: 11': 'prec_12_18h', 'Unnamed: 12': 'prec_18_24h',
           'Unnamed: 13': 'fecha'}

dataset.rename(columns=columns, inplace=True)
print(f'{dataset}\n')


# Quite de las columnas que contengan la hora y deje solo la parte numérica. 9.6 (02:20) -> 9.6 -- 5
dataset = dataset.replace(to_replace=r'\s+\(\d+:\d+\)', value='', regex=True)
print(f'{dataset}\n')


# La nueva columna que se renombró como "fecha" contiene toda la ruta fuente del archivo, elimine todas las cadenas y deje solo la fecha. El formato que debe quedar es por ejemplo: 2019-01-15 -- 6
dataset['fecha'] = dataset['AEMET FILENAMES'].str.split('t').str[-1].str[:-4]
print(f'{dataset}\n')


# Muestre los tipos de datos actuales del dataset -- 7
print(f'{dataset.dtypes}\n')


# Se observa que hay varios tipos de datos "object", cuando debería ser un float (por ejemplo: temp_max y viento racha). Esto es porque hay filas que no tienen valor para esas columnas, 
# luego veremos que hacer con ellas. Por ahora asigne los tipos de datos adecuados a cada columna.
# -- 8
dataset['estacion'] = dataset['estacion'].astype('string')
dataset['provincia'] = dataset['provincia'].astype('string')
dataset['temp_max'] = pd.to_numeric(dataset['temp_max'], errors='coerce')
dataset['temp_min'] = pd.to_numeric(dataset['temp_min'], errors='coerce')
dataset['viento_racha'] = pd.to_numeric(dataset['viento_racha'], errors='coerce')
dataset['viento_vel_max'] = pd.to_numeric(dataset['viento_vel_max'], errors='coerce')
dataset['fecha'] = dataset['fecha'].astype('datetime64[ns]')
print(f'{dataset.dtypes}\n')


# Elimine las estaciones que tienen filas a las que les faltan datos para estandarizar los datos. -- 9
dataset = dataset.dropna()
print(f'{dataset}\n')


# Ahora que tenemos los datos limpios, muestre con "describe" las medidas de nuestros datos. -- 10
descripcion = dataset.describe()
print(f'{descripcion}\n')


# Muestre 5 filas al azar como muestreo de los datos. También es un ejemplo de selección de columnas por expresión regular (seleccionamos las que empiezan por el prefijo "temp_") -- 11
muestreo_aleatorio = dataset.sample(n=5, random_state=42)
print("5 filas aleatorias:")
print(muestreo_aleatorio)

columnas_temp = dataset.filter(regex=r'^temp_', axis=1)
print("\nColumnas con 'temp_':")
print(columnas_temp)


# Muestre la media de los valores de cada columna agrupando por provincia. Observe que el método es lo suficientemente inteligente para mostrarnos solo columnas de tipo numérico. -- 12
# Seleccionar solo las columnas numéricas
colum_tipo_numerico = ['temp_max', 'temp_min', 'viento_racha', 'viento_vel_max']
media_provincial = dataset.groupby('provincia')[colum_tipo_numerico].mean()
print(media_provincial)


# Muestre los 3 valores más altos de temperatura máxima que se han registrado en el mes. Es un ejemplo de cómo ordenar por columna, muestre solo las columnas que nos interesa y de esas columnas muestre solo las 3 primeras filas. 
# -- 13
top_temp_max = dataset.nlargest(3, 'temp_max')[['provincia', 'fecha', 'temp_max']]
print(f'{top_temp_max}\n')


# De forma similar obtenga los 3 valores más bajos de temperatura mínima. -- 14
bottom_temp_min = dataset.nsmallest(3, 'temp_min')[['provincia', 'fecha', 'temp_min']]
print(f'{bottom_temp_min}\n')

# Calcule en una nueva columna restando de la temperatura máxima la temperatura mínima. Observe que simplemente restamos columnas. -- 15
dataset['operacion_columna'] = dataset['temp_max'] - dataset['temp_min']
print(f'{dataset.head()}\n')


# Agrupe por una columna (provincia) y obtenga el máximo de los valores de otra columna (viento_racha) para cada grupo y ordene posteriormente esas filas. -- 16
# Agrupar por la columna 'provincia' y obtener el máximo de 'viento_racha' para cada grupo
max_viento_racha_por_provincia = dataset.groupby('provincia')['viento_racha'].max().reset_index().sort_values(by='viento_racha', ascending=False)
print(max_viento_racha_por_provincia)


# Hacemos de forma similar el cálculo de las mayores velocidades de viento medio en un día por provincia. -- 17
viento_medio= dataset.groupby('provincia')['viento_vel_max'].mean().reset_index()
max_viento_medio = viento_medio.groupby('provincia')['viento_vel_max'].max().reset_index().sort_values(by='viento_vel_max', ascending=False)
max_viento_medio.rename(columns={'viento_vel_max': 'viento_med_max'}, inplace=True)
print(max_viento_medio)


# Calcular la media por grupo de la forma más fácil e intuitiva posible (con "group" y "mean"). -- 18
# Calcular la media de 'viento_vel_max' por grupo (en este caso, grupo 'provincia')
dataIntencion = ['estacion', 'provincia', 'temp_max', 'temp_min', 'temp_med', 'viento_racha', 'viento_vel_max', 'prec_dia', 'prec_0_6h', 'prec_6_12h', 'prec_12_18h','fecha']
for columna in dataIntencion:
    media_por_grupo = dataset.groupby(columna)['viento_vel_max'].mean()
    print(f"Media de 'viento_vel_max' agrupado por {columna}:\n{media_por_grupo}\n")


# Realice una operación de restar entre la fila actual y la fila anterior usando "shift" (desplaza una fila hacia abajo) -- 19
dataset['temp_max_shifted'] = dataset['temp_max'] - dataset.groupby('estacion')['temp_max'].shift()
top_diff = dataset.groupby('provincia')['temp_max_shifted'].idxmax()
print(dataset.loc[top_diff].sort_values(by='temp_max_shifted', ascending=False)[['fecha', 'estacion', 'provincia', 'temp_max_shifted']].head(5))
