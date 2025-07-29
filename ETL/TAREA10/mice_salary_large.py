
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Crear el conjunto de datos con valores faltantes
data = pd.read_csv("C:/workspace/Python/TAREA10/data/Salary.csv")

df = pd.read_csv("C:/workspace/Python/TAREA10/data/Salary.csv")

# Imputación por la media
df["YearsExperience"].fillna(df["YearsExperience"].mean(), inplace=True)

# Imputación mediante regresión lineal
def impute_years_experience(data):
    for i in range(len(data)):
        if pd.isnull(data.loc[i, "YearsExperience"]):
            # Crear un modelo de regresión lineal
            model = LinearRegression()
            known = data.dropna()  # Excluir filas con valores faltantes
            X = known["Salary"].values.reshape(-1, 1)
            y = known["YearsExperience"].values
            model.fit(X, y)
            
            # Predecir el valor faltante
            X_pred = np.array(data.loc[i, "Salary"]).reshape(1, -1)
            y_pred = model.predict(X_pred)
            data.loc[i, "YearsExperience"] = y_pred[0]
    
    return data

# Realizar varias iteraciones para mejorar las estimaciones
num_iterations = 5  # Ajusta este valor según tu necesidad
for _ in range(num_iterations):
    df = impute_years_experience(df)

print("Conjunto de datos original con valores faltantes:")
print(data)

print("\nConjunto de datos imputado paso a paso:")
print(df)
