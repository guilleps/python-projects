import os
import pandas as pd

# Ruta al directorio que contiene los archivos .xls
directorio = 'C:/workspace/Python/TAREA4/csv_tarea4/'

# Crear una lista para almacenar los DataFrames de cada archivo
dataframes = []

# Iterar a través de los archivos en el directorio
for archivo in os.listdir(directorio):
    if archivo.endswith(".xls"):
        # Leer el archivo xls y almacenarlo en un DataFrame
        df = pd.read_excel(os.path.join(directorio, archivo))
        
        # Agregar una nueva columna con el nombre del archivo
        df['AEMET FILENAMES'] = archivo
        
        # Agregar el DataFrame a la lista
        dataframes.append(df)

# Combinar todos los DataFrames en uno solo
dataset = pd.concat(dataframes, ignore_index=True)

