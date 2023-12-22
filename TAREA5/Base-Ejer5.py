import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats

# Obtener la ruta completa del archivo CSV
csv_file = 'C:/workspace/Python/TAREA5/data/BL-Flickr-Images-Book.csv'
csv_path = os.path.abspath(csv_file)

# Verificar si el archivo CSV existe antes de cargarlo
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"El archivo CSV '{csv_file}' no se encuentra en el directorio actual.")

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(csv_path)

# 2. Usar heatmap para visualizar datos con valores nulos
sns.heatmap(df.isnull(), cbar=False, cmap='magma')
plt.show()

# 3. Detectar valores perdidos con isna() y isnull()
missing_values = df.isna()  # Tener en cuenta estas sintaxis -> isna() y isnull() son iguales y tienen la misma funcion

# 4. Contar el número de datos perdidos
total_missing = missing_values.values.sum()

# 5. Contar el número de filas con datos perdidos
rows_with_missing = missing_values.any(axis=1).sum()

# 6. Contar el número de columnas con datos perdidos
cols_with_missing = missing_values.any().sum()

# 7. Determinar el número de registros duplicados por una columna
duplicates_by_column = df['xxx'].duplicated().sum()    #Remplazar xxx por la columna a trabajar

# 8. Determinar el número de registros duplicados por dos columnas
duplicates_by_two_columns = df[['xxx', 'xxx']].duplicated().sum()   #Remplazar xxx por la columna a trabajar

# 9. Eliminar filas con datos perdidos usando dropna(how='any')
df_cleaned = df.dropna(how='any')

# 10. Reemplazar valores faltantes con la media (usar en una columna numérica)
column_to_fill = 'xxx'    #Remplazar xxx por la columna a trabajar
mean_value = df[column_to_fill].mean()
df[column_to_fill].fillna(mean_value, inplace=True)

# 11. Limpiar valores atípicos usando Z-Score
z_scores = stats.zscore(df['xxx'])    #Remplazar xxx por la columna a trabajar
df_no_outliers = df[(z_scores < 3) & (z_scores > -3)]

# 12. Usar el método drop_duplicates() para eliminar valores duplicados
df_no_duplicates = df.drop_duplicates()

# Mostrar las respuestas
print("Total de datos perdidos:", total_missing)
print("Número de filas con datos perdidos:", rows_with_missing)
print("Número de columnas con datos perdidos:", cols_with_missing)
print("Número de registros duplicados por una columna:", duplicates_by_column)
print("Número de registros duplicados por dos columnas:", duplicates_by_two_columns)
