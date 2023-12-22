import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Carga tu conjunto de datos (asegúrate de que los modelos de regresión para "Age" y "Balance" se hayan construido en el Paso 3)
data = pd.read_csv("TAREA10/data/Churn_Modelling.csv")

# Reemplazar los 0 con NaN para que sean tratados como valores faltantes
data['Age'] = data['Age'].replace(0, np.nan)
data['Balance'] = data['Balance'].replace(0, np.nan)

# Paso 1: Eliminar las filas con valores faltantes
data.dropna(subset=['Age', 'Balance'], inplace=True)

# Obtener una lista de las columnas con valores faltantes
columns_with_missing_values = data.columns[data.isnull().any()].tolist()

# Definir el número de ciclos (iteraciones) para repetir el proceso
num_cycles = 10  # Puedes ajustar este número según tus necesidades

for _ in range(num_cycles):
    for column in columns_with_missing_values:
        # Paso 2: Restablecer las imputaciones de la media con NaN
        data[column].fillna(pd.NA, inplace=True)

        # Paso 3: Realizar la regresión lineal para imputar los valores faltantes
        regression_model = LinearRegression()
        
        # Variables independientes (todas las demás columnas)
        independent_columns = [col for col in data.columns if col != column]
        
        X = data[independent_columns]
        y = data[column]

        # Filtrar las filas con valores observados de "column" y otras variables
        X_notnull = X[y.notnull()]
        y_notnull = y[y.notnull()]
        
        regression_model.fit(X_notnull, y_notnull)

        # Filtrar las filas con valores faltantes de "column" y otras variables
        X_to_impute = X[y.isna()]
        
        # Paso 4: Predicciones para los valores faltantes de "column"
        y_imputed = regression_model.predict(X_to_impute)

        # Reemplazar los valores faltantes de "column" con las predicciones
        data.loc[data[column].isna(), column] = y_imputed

# Mostrar las primeras 16 filas con los valores imputados
selected_fields = data[['Age', 'Balance', 'Exited']]
print(selected_fields.head(16))
