import numpy as np
import pandas as pd

df = pd.read_csv("TAREA11/data/dataset_calificaciones.csv")

# Calcular la media y la desviación estándar de Calificacion_Examen
media_calificacion = np.mean(df['Calificacion_Examen'])
desviacion_std_calificacion = np.std(df['Calificacion_Examen'])

print('La media de Calificacion_Examen es:', media_calificacion)
print('La desviación estándar de Calificacion_Examen es:', desviacion_std_calificacion)

# Identificar outliers en Calificacion_Examen
umbral_z = 3
outliers_calificacion = []

for calificacion in df['Calificacion_Examen']:
    z_score = (calificacion - media_calificacion) / desviacion_std_calificacion
    if z_score > umbral_z:
        outliers_calificacion.append(calificacion)

print('Los outliers en Calificacion_Examen son:')
print(outliers_calificacion)