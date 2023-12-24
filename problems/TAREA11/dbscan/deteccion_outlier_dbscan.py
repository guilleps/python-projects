import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("TAREA11/dbscan/data/dataset_calificaciones.csv")

X = df[['Horas_de_Estudio', 'Calificacion_Examen']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dbscan = DBSCAN(eps=0.30, min_samples=10)  # Puedes ajustar eps y min_samples según tu necesidad
labels = dbscan.fit_predict(X_scaled)

df['Cluster'] = labels

plt.figure(figsize=(12, 6))

normal = plt.scatter(df[df['Cluster'] != -1]['Horas_de_Estudio'], 
                     df[df['Cluster'] != -1]['Calificacion_Examen'], 
                     c=df[df['Cluster'] != -1]['Cluster'], cmap='viridis', s=10, label='Datos Normales')  # type: ignore

outliers = plt.scatter(df[df['Cluster'] == -1]['Horas_de_Estudio'], 
                       df[df['Cluster'] == -1]['Calificacion_Examen'], 
                       c='red', marker='x', s=50, label='Datos Atípicos')

plt.title('DBSCAN Clusterizacion (2D)')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificación en el Examen')
plt.legend(handles=[normal, outliers], title='Clusters')
plt.show()

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

normal_3d = ax.scatter(df[df['Cluster'] != -1]['Horas_de_Estudio'], 
                       df[df['Cluster'] != -1]['Calificacion_Examen'], 
                       df[df['Cluster'] != -1]['Cluster'], 
                       c=df[df['Cluster'] != -1]['Cluster'], 
                       cmap='viridis', s=10, label='Datos Normales') # type: ignore

outliers_3d = ax.scatter(df[df['Cluster'] == -1]['Horas_de_Estudio'], 
                         df[df['Cluster'] == -1]['Calificacion_Examen'], 
                         df[df['Cluster'] == -1]['Cluster'], 
                         c='red', marker='x', s=50, label='Datos Atípicos') # type: ignore

ax.set_xlabel('Horas de Estudio')
ax.set_ylabel('Calificación en el Examen')
ax.set_zlabel('Cluster') # type: ignore
plt.title('DBSCAN Clusterizacion (3D)')
ax.legend(handles=[normal_3d, outliers_3d], title='Clusters')
plt.show()
