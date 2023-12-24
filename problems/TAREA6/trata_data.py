import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y crear DataFrame
df = pd.read_csv('C:/workspace/Python/TAREA6/data/treatments.csv', sep=',')

# print(df.info())

# # Número de filas y columnas
# num_filas, num_columnas = df.shape
# print(f'El DataFrame tiene: \n {num_filas} filas \n {num_columnas} columnas')

# # Buscar filas duplicados
# print(df.duplicated().any())
# # True si hay datos duplicados, False si no los hay

# # Tipos de datos de cada columna
# print('Tipos de datos por columna:\n', df.dtypes)

# # Detectar valores nulos en cada columna
# print('Valores nulos por columna:\n', df.isnull().sum())

# # Detectar valores perdidos y contarlos
# missingValues = df.isna()
# num_missing = missingValues.values.sum()
# plt.title(f'Número total de datos perdidos: {num_missing}', fontsize=14, pad=20)
# sns.heatmap(df.isna(), cbar=False, cmap='magma')
# plt.show()

# ##################################################3333

# df['given_name'] = df['given_name'].astype('string')
# df['surname'] = df['surname'].astype('string')
# df['auralin'] = df['auralin'].astype('string')
# df['novodra'] = df['novodra'].astype('string')
# print('Formato actualizado:\n', df.dtypes)

# # Crear listas para almacenar los valores de medicamento y dosis
# medicamento = []
# dosis = []

# # Iterar sobre las filas del DataFrame
# for index, row in df.iterrows():
 
#  if not pd.isnull(row['auralin']) and row['auralin'] != '-' and row['auralin'] is not None:
#     medicamento.append('auralin')
#     dosis.append(row['auralin'])
#  # Verificar si la columna novodra está llena y no es None o '-'
#  elif not pd.isnull(row['novodra']) and row['novodra'] != '-' and row['novodra'] is not None:
#     medicamento.append('novodra')
#     dosis.append(row['novodra'])

# df.insert(df.columns.get_loc('hba1c_start'),'Medicamento',medicamento)
# df.insert(df.columns.get_loc('hba1c_start'),'Dosis',dosis)
# df.drop(['auralin','novodra'],axis = 1, inplace=True)
# print(df)

# Renombrar nombre de columnas
df.rename(columns={
    'given_name': 'Nombre',
    'surname': 'Apellido',
    'hba1c_start': 'Prueba de sangre inicial',
    'hba1c_end': 'Prueba de sangre final',
    'hba1c_change': 'Variacion'
}, inplace=True)
print(df)

df = df.drop(columns=['Variacion'])

# Calcula la nueva columna 'Variacion' restando las pruebas de sangre inicial y final
df['Variacion'] = df['Prueba de sangre inicial'] - df['Prueba de sangre final']
print(df)

# Calcula el número de valores negativos en la columna 'Variacion'
num_valores_negativos = (df['Variacion'] < 0).sum()
print("")
print(f"Hay {num_valores_negativos} valores negativos en la columna 'Variacion'.")
print("")

# Agrega una nueva columna 'Efecto' basada en la columna 'Variacion'
df['Efecto'] = ['Positivo' if variacion >= 0 else 'Negativo' for variacion in df['Variacion']]
print(df)

# Capitaliza la primera letra de los nombres y apellidos sin usar lambda
df['Nombre'] = df['Nombre'].str.title()
df['Apellido'] = df['Apellido'].str.title()
print(df)



