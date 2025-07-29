import pandas as pd

df = pd.read_csv("C:/workspace/Python/TAREA3/csv_tarea3/titanic.csv")

num_filas, num_columnas = df.shape 
print("\nDimensiones del DataFrame:")
print("\nNumero de filas:", num_filas)
print("\nNumero de columnas:", num_columnas)
print("\nNúmero de datos en el DataFrame:", df.size)
print("\nNombres de las columnas:", df.columns)
print("\nNombres de las filas (índices):", df.index)
print("\nTipos de datos de las columnas:\n", df.dtypes)
print("\nPrimeras 10 filas:\n", df.head(10))
print("\nÚltimas 10 filas:\n", df.tail(10))

print("\nDatos del pasajero con identificador 148:\n", df.loc[148])

print("\nFilas pares:\n", df.iloc[1::2])

print("\n de personas en primera clase ordenados alfabéticamente:")
first_class_names = df[df['Pclass'] == 1]['Name'].sort_values()
print(first_class_names)

survival_counts = df['Survived'].value_counts(normalize=True) * 100
print("\nPorcentaje de personas que sobrevivieron:\n", survival_counts[1], "%")
print("\nPorcentaje de personas que murieron:\n", survival_counts[0], "%")

survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
print("\nPorcentaje de personas que sobrevivieron en cada clase:\n", survival_by_class)

df.dropna(subset=['Age'], inplace=True)

mean_age_by_class_gender = df.groupby(['Pclass', 'Sex'])['Age'].mean()
print("\nEdad media de mujeres por clase:\n", mean_age_by_class_gender)

df['EsMenor'] = df['Age'] < 18

survival_by_class_age = df.groupby(['Pclass', 'EsMenor'])['Survived'].mean() * 100
print("\nPorcentaje de menores y mayores de edad que sobrevivieron en cada clase:\n", survival_by_class_age)

