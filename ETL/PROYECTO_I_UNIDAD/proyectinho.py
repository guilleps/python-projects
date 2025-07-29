import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y crear DataFrame
df = pd.read_csv('C:/workspace/Python/PROYECTO/datos/AB_NYC_2019.csv', sep=',')

#print(df)

#*******************************EXPLORACIÓN*******************************
"""
print(df.info())

print(df.describe())

# Número de filas y columnas
num_filas, num_columnas = df.shape
print(f'El DataFrame tiene: \n {num_filas} filas \n {num_columnas} columnas')

# Buscar filas duplicados
print(df.duplicated().any())
# True si hay datos duplicados, False si no los hay

# Tipos de datos de cada columna
print('Tipos de datos por columna:\n', df.dtypes)

# Cuenta de valores únicos para características categóricas
print(df['neighbourhood_group'].value_counts())
print(df['room_type'].value_counts())

# Detectar valores nulos en cada columna
print('Valores nulos por columna:\n', df.isnull().sum())

# Detectar valores perdidos y contarlos
missingValues = df.isna()
num_missing = missingValues.values.sum()

plt.title(f'Número total de datos perdidos: {num_missing}', fontsize=14, pad=20)
sns.heatmap(df.isna(), cbar=False, cmap='magma')
plt.show()
"""


#*******************************TRANSFORMACIÓN*******************************

# Renombrar nombre de columnas
df.rename(columns={
    'id': 'ID',
    'name': 'Nombre de Estancia',
    'host_id': 'ID Host',
    'host_name': 'Nombre del Host',
    'neighbourhood_group': 'Ciudad',
    'neighbourhood': 'Area',
    'latitude': 'Latitud',
    'longitude': 'Longitud',
    'room_type': 'Tipo de Estancia',
    'price': 'Precio',
    'minimum_nights': 'Noches minimas',
    'number_of_reviews': 'Cantidad de visitas',
    'last_review': 'Ultima visita',
    'reviews_per_month': 'Visitas mensuales',
    'calculated_host_listings_count': 'Calificacion del Host',
    'availability_365': 'Disponibilidad Anual'
}, inplace=True)

#print(df.columns)

# Eliminar columnas innecesarios
columnas_a_eliminar = [
    'ID', 'ID Host', 'Nombre del Host', 'Latitud', 
    'Longitud', 'Ultima visita', 'Calificacion del Host'
]
df.drop(columnas_a_eliminar, axis=1, inplace=True)

#print(df.columns)

# Discretizar conjunto de datos continuos (Disponibilidad)
bins = [0, 1, 50, 200, 366]
labels = ['No disponibilidad', 'Baja disponibilidad', 'Media disponibilidad', 'Alta disponibilidad']

df['Tipo de Disponibilidad'] = pd.cut(df['Disponibilidad Anual'], bins=bins, labels=labels, right=False)
#print(df[['Disponibilidad Anual', 'Tipo de Disponibilidad']])

# Discretizar conjunto de datos continuos (Precio)
#print("Precio máximo:", df['Precio'].max())
#print("Precio mínimo:", df['Precio'].min())

#print(f'Número de filas con precio igual a 0: ', (df['Precio'] == 0).sum())

df = df.drop(df[df['Precio'] == 0].index)



bins = [10, 1000, 5000, 10001]
categorias = ['Estándar', 'Ejecutivo', 'Premium']

df['Categoría de Estancia'] = pd.cut(df['Precio'], bins=bins, labels=categorias, right=False)
#print(df[['Precio', 'Categoría de Estancia']])
#print(df['Categoría de Estancia'].value_counts())

# Discretizar conjunto de datos continuos (Nomches mínimas)

#print(df['Noches minimas'].unique())

#Antes
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6)) 
sns.boxplot(x=df['Noches minimas'], color='skyblue')

plt.title("Boxplot de Noches Mínimas con Datos Atípicos")
plt.xlabel("Noches Mínimas")
#plt.show()

#Después
df = df[df['Noches minimas'] <= 365]
#print(df['Noches minimas'].max())

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6)) 
sns.boxplot(x=df['Noches minimas'], color='skyblue')

plt.title("Boxplot de Noches Mínimas sin Datos Atípicos")
plt.xlabel("Noches Mínimas")
#plt.show()

bins = [0, 31, 150, 300, 366]
labels = ['Mínimo', 'Promedio', 'Superior al Promedio', 'Excepcional']

df['Categoría de Noches minimas'] = pd.cut(df['Noches minimas'], bins=bins, labels=labels, right=False)
#print(df[['Noches minimas', 'Categoría de Noches minimas']])
#print(df['Categoría de Noches minimas'].value_counts())

# Cambiar formato de datos
#print('Tipos de datos por columna:\n', df.dtypes)

df['Nombre de Estancia'] = df['Nombre de Estancia'].astype('string')
df['Ciudad'] = df['Ciudad'].astype('string')
df['Area'] = df['Area'].astype('string')
df['Tipo de Estancia'] = df['Tipo de Estancia'].astype('string')
df['Precio'] = df['Precio'].astype(float)  

#print('Formato actualizado:\n', df.dtypes)

# Calcula valores nulos
#print('Valores nulos por columna:\n', df.isnull().sum())

Vista_mensual_mean = df['Visitas mensuales'].mean()
df['Visitas mensuales'].fillna(Vista_mensual_mean, inplace=True)
#print(df[['Visitas mensuales']].isnull().sum())

# Elimina filas con datos perdidos en las columnas 'name'
df.dropna(subset=['Nombre de Estancia'], inplace=True)
#print(df[['Nombre de Estancia']].isnull().sum())

missingValues = df.isna()
num_missing = missingValues.values.sum()

plt.title(f'Número total de datos perdidos: {num_missing}', fontsize=14, pad=20)
sns.heatmap(df.isna(), cbar=False, cmap='magma')
#plt.show()

#*******************************ANÁLISIS*******************************


# Máximo y mínimo
print("Precio máximo:", df['Precio'].max())
print("Precio mínimo:", df['Precio'].min())


# Media, mediana y moda
print("Precio medio:", df['Precio'].mean())
print("Precio mediana:", df['Precio'].median())
print("Precio moda:", df['Precio'].mode()[0])


# Calcular precios por ciudad
precios_por_ciudad = df.groupby('Ciudad')['Precio'].agg(['max', 'min', 'mean']).reset_index()
print(precios_por_ciudad)

plt.figure(figsize=(10, 6))
sns.barplot(x='Ciudad', y='mean', data=precios_por_ciudad, color='skyblue', label='Promedio')
plt.errorbar(x=precios_por_ciudad['Ciudad'], y=precios_por_ciudad['mean'],
             yerr=[precios_por_ciudad['mean'] - precios_por_ciudad['min'], precios_por_ciudad['max'] - precios_por_ciudad['mean']],
             fmt='none', color='black', capsize=5)
plt.ylabel('Precio')
plt.title('Precio Máximo, Mínimo y Promedio por Ciudad')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# Máximo y mínimo
print("Noches mínimas máximo:", df['Noches minimas'].max())
print("Noches mínimas mínimo:", df['Noches minimas'].min())


# Media, mediana y moda
print("Noches mínimas medio:", df['Noches minimas'].mean())
print("Noches mínimas mediana:", df['Noches minimas'].median())
print("Noches mínimas moda:", df['Noches minimas'].mode()[0])

# Calcular noches minimas por tipo de estancia
ciudad_noches_minimas = df.groupby('Ciudad')['Noches minimas'].agg(['max', 'min', 'mean']).reset_index()
print(ciudad_noches_minimas)

plt.figure(figsize=(10, 6))
sns.barplot(x='Ciudad', y='mean', data=ciudad_noches_minimas, color='skyblue', label='Promedio')
plt.errorbar(x=ciudad_noches_minimas['Ciudad'], y=ciudad_noches_minimas['mean'],
             yerr=[ciudad_noches_minimas['mean'] - ciudad_noches_minimas['min'], ciudad_noches_minimas['max'] - ciudad_noches_minimas['mean']],
             fmt='none', color='black', capsize=5)
plt.ylabel('Noches mínimas')
plt.title('Noches Mínimas Máximo, Mínimo y Promedio por Ciudad')
plt.xticks(rotation=45)
plt.legend()
plt.show()


# Gráfico de barras para la columna 'Ciudad' y sumar la cantidad de visitas por cada una
ciudad_visitas = df.groupby('Ciudad')['Cantidad de visitas'].sum().reset_index()
print(ciudad_visitas)

plt.figure(figsize=(10, 6))
plt.bar(ciudad_visitas['Ciudad'], ciudad_visitas['Cantidad de visitas'], color='skyblue')
plt.xlabel('Ciudad')
plt.ylabel('Total de Visitas')
plt.title('Total de Visitas por Ciudad')
plt.xticks(rotation=45)

plt.show()

# Gráfico de barras para cada ciudad según disponibilidad de estancias
estancias_por_categoria = df.groupby(['Ciudad', 'Tipo de Disponibilidad'], observed=False).size().reset_index(name='Número de Estancias')
print(estancias_por_categoria)

g = sns.catplot(x='Ciudad',hue='Tipo de Disponibilidad',data=df,kind='count',palette='Set2',height=6,aspect=1.5)
g.set(xlabel='Ciudad',ylabel='Número de Estancias',title='Distribución de Estancias por Tipo de Disponibilidad')
plt.show()


# Agrupar por ciudad y tipo de estancia y contar el número de estancias en cada categoría
estancias_por_ciudad_tipo = df.groupby(['Ciudad', 'Tipo de Estancia']).size().reset_index(name='Cantidad de Estancias')
print(estancias_por_ciudad_tipo)

plt.figure(figsize=(10, 6))
sns.barplot(x='Ciudad', y='Cantidad de Estancias', hue='Tipo de Estancia', data=estancias_por_ciudad_tipo, palette='colorblind')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de Estancias')
plt.title('Cantidad de Estancias por Ciudad y Tipo de Estancia')
plt.xticks(rotation=45)
plt.legend(title='Tipo de Estancia')
plt.show()


# Pastel general de visitas mensuales
categorias_agrupadas = df['Categoría de Estancia'].replace(['Ejecutivo', 'Premium'], 'Otras Categorías')

plt.figure(figsize=(8, 8))
plt.pie(categorias_agrupadas.value_counts(), 
        labels=categorias_agrupadas.unique(), autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
plt.title('Visitas Mensuales por Categoría de Estancia')
plt.show()

# Obtener las ciudades únicas en el DataFrame
df['Categoría de Estancia'] = df['Categoría de Estancia'].replace(['Ejecutivo', 'Premium'], 'Otras Categorías')
ciudades_unicas = df['Ciudad'].unique()

for ciudad in ciudades_unicas:
    datos_ciudad = df[df['Ciudad'] == ciudad]
    categorias_agrupadas = datos_ciudad['Categoría de Estancia']
    
    plt.figure(figsize=(6, 6)) 
    plt.pie(categorias_agrupadas.value_counts(), 
            labels=categorias_agrupadas.unique(),autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set2'))
    
    plt.title(f'Visitas Mensuales por Categoría de Estancia en {ciudad}')
    plt.show()




