import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Cargar el conjunto de datos desde el archivo CSV
df = pd.read_csv("TAREA11/isolation_forest/data/dataset_calificaciones.csv")

# Seleccionar las columnas relevantes para la detección de anomalías
X = df[['Horas_de_Estudio', 'Calificacion_Examen']]

# Crear y ajustar el modelo Isolation Forest
iso_forest = IsolationForest(contamination=0.1, n_estimators=100)  # Puedes ajustar el parámetro de contaminación según tu necesidad
labels = iso_forest.fit_predict(X)

# Agregar las etiquetas al DataFrame
df['Anomalia'] = labels

# Visualización de los resultados en 2D
plt.figure(figsize=(12, 6))

# Visualización de los datos normales
normal = plt.scatter(df[df['Anomalia'] != -1]['Horas_de_Estudio'], 
                     df[df['Anomalia'] != -1]['Calificacion_Examen'], 
                     c=df[df['Anomalia'] != -1]['Anomalia'], cmap='viridis', s=10, label='Datos Normales') # type: ignore

# Visualización de las anomalías
anomalias = plt.scatter(df[df['Anomalia'] == -1]['Horas_de_Estudio'], 
                        df[df['Anomalia'] == -1]['Calificacion_Examen'], 
                        c='red', marker='x', s=50, label='Anomalías')

plt.title('Resultado de Isolation Forest (2D)')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación en el Examen')
plt.legend(handles=[normal, anomalias], title='Anomalías')
plt.show()
