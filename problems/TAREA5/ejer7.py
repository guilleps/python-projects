import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv')

# Elegir las dos columnas por las cuales buscar duplicados
column1_name = 'Engraver'  # Reemplaza 'nombre_columna1' con el nombre de la primera columna
column2_name = 'Author'  # Reemplaza 'nombre_columna2' con el nombre de la segunda columna

# Contar los registros duplicados en esas dos columnas
duplicates_count = df[df.duplicated(subset=[column1_name, column2_name])].shape[0]

# Imprimir el número de registros duplicados
print(f"El número de registros duplicados en las columnas '{column1_name}' y '{column2_name}' es: {duplicates_count}")
