import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("C:/workspace/Python/TAREA9_1/data/Salary.csv")

print(f'Presentación del dataset original')
print(df)
print("\n")

print(f'Descripcion del dataset')
print(df.describe())
print("\n")

print('Valores nulos por columna: ')
print(df.isnull().sum())
print("\n")


# Elimina filas con valores faltantes
data = df.dropna()

# Selecciona las variables independiente (x) y dependiente (y)
x = data["YearsExperience"]
y = data["Salary"]

# Realiza la regresión lineal y obtén los resultados, incluyendo R^2
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Función de regresión lineal
def linear_regression(x):
    return slope * x + intercept

# Predicciones
predicted_y = linear_regression(x)

# Gráfico de dispersión de los datos y la línea de regresión
plt.scatter(x, y, label='Datos')
plt.plot(x, predicted_y, color='red', label='Regresión Lineal')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')
plt.legend()
plt.show()

# Calcula el coeficiente de determinación R^2
r_squared = r_value ** 2

print("Coeficiente de Determinación (R^2):", r_squared)
print("\n")


# Crea un DataFrame df_sin_na excluyendo filas con valores nulos
df_sin_na = df.dropna()

# Crea un modelo de regresión lineal
modelo = LinearRegression()

# Ajusta el modelo a los datos sin valores nulos
modelo.fit(df_sin_na[['Salary']], df_sin_na['YearsExperience'])

# Obtiene la pendiente (coeficiente) y el intercepto
pendiente = modelo.coef_[0]
intercepto = modelo.intercept_

print(f"Pendiente (Coeficiente): {pendiente}")
print(f"Intercepto: {intercepto}")
print("\n")



df['YearsExperience'] = df['YearsExperience'].fillna(pendiente * df['Salary'] + intercepto)
df.isnull().sum()

print(df)
print("\n")

print('Valores nulos por columna: ')
print(df.isnull().sum())
print("\n")

