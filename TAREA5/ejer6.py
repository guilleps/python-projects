import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Elegir la columna por la cual buscar duplicados
column_name = 'Publisher'  # Reemplaza 'nombre_de_la_columna' con el nombre de la columna que deseas verificar

# Contar los registros duplicados en esa columna
duplicates_count = df[df.duplicated(subset=column_name)].shape[0]

# Imprimir el número de registros duplicados
print(f"El número de registros duplicados en la columna '{column_name}' es: {duplicates_count}")

# #####################################33

# Elegir la columna por la cual buscar duplicados
column_name = 'Edition Statement'  # Reemplaza 'nombre_de_la_columna' con el nombre de la columna que deseas verificar

# Contar los registros duplicados en esa columna
duplicates_count = df[df.duplicated(subset=column_name)].shape[0]

# Imprimir el número de registros duplicados
print(f"El número de registros duplicados en la columna '{column_name}' es: {duplicates_count}")