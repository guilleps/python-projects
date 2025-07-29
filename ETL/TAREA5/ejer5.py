import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Contar el número de columnas con datos perdidos
columns_with_missing_data = df.columns[df.isnull().any()]
total_columns_with_missing_data = len(columns_with_missing_data)

# Imprimir el total de columnas con datos perdidos
print(f"El número de columnas con datos perdidos es: {total_columns_with_missing_data}")

