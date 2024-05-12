import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Contar el número de filas con datos perdidos
rows_with_missing_data = df[df.isnull().any(axis=1)]
total_rows_with_missing_data = len(rows_with_missing_data)

# Imprimir el total de filas con datos perdidos
print(f"El número de filas con datos perdidos es: {total_rows_with_missing_data}")
