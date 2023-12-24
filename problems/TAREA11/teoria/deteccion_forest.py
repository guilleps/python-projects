import pandas as pd
from sklearn.ensemble import IsolationForest

# Cargamos un conjunto de datos (Mall_Customers.csv)
data = pd.read_csv("TAREA11/data/mall_customers.csv")
x = data.loc[:, ['Annual Income (k$)', 'Spending Score (1-100)']].values

# Configuramos y ajustamos el modelo Isolation Forest
iso_forest = IsolationForest(contamination=0.05)  # Puedes ajustar la contaminación según tu conjunto de datos
iso_forest.fit(x)
outliers = iso_forest.predict(x)

# Los valores atípicos son -1 en la salida
atipicos = x[outliers == -1]

print('Valores atípicos detectados:', atipicos)
