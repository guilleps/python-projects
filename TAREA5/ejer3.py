import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

missingValues = df.isnull()

# Sumar los valores True (valores nulos) en la matriz para contarlos
total_missing = missingValues.values.sum()

# Imprimir el total de valores nulos
print(f"El número total de datos perdidos en el DataFrame es: {total_missing}")