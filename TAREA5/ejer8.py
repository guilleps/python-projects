import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Eliminar filas con datos perdidos en cualquier columna
df_cleaned = df.dropna(how='any')

# df_cleaned ahora contiene el DataFrame sin filas que tengan valores nulos en cualquier columna

# Puedes imprimir df_cleaned para verificar el resultado
print(df_cleaned)
