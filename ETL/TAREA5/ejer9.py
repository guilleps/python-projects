import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Reemplazar valores faltantes con la media en una columna numérica
column_name = 'Identifier'  # Reemplaza 'nombre_de_la_columna' con el nombre de la columna deseada

# Calcula la media de la columna
mean_value = df[column_name].mean()

# Reemplaza los valores faltantes con la media
df[column_name].fillna(mean_value, inplace=True)

# Ahora, df contiene la columna 'nombre_de_la_columna' con valores faltantes reemplazados por la media
