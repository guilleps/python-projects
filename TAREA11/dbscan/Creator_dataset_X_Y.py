import pandas as pd
import numpy as np

# Configurar la semilla para reproducibilidad
np.random.seed(42)

# Generar datos para el conjunto de datos
num_records = 9516

# Horas de estudio (entre 5 y 16 horas)
horas_de_estudio = np.random.uniform(5, 16, num_records)

# Calificación en el examen (entre 0 y 20 con algunos datos atípicos dispersos entre 20 y 100)
calificacion_examen = np.random.uniform(0, 20, num_records)
atipicos_indices_exam = np.random.choice(num_records, 69, replace=False)
calificacion_examen[atipicos_indices_exam] = np.random.uniform(22, 36, 69)

# Agregar datos atípicos para las horas de estudio (entre 19 y 23 horas)
atipicos_indices_horas = np.random.choice(num_records, 452, replace=False)
horas_de_estudio[atipicos_indices_horas] = np.random.uniform(19, 23, 452)

# Crear una sección para los alumnos (A, B, C)
secciones = np.random.choice(['A', 'B', 'C'], num_records)

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'Horas_de_Estudio': horas_de_estudio,
    'Calificacion_Examen': calificacion_examen,
    'Seccion': secciones
})

# Guardar el DataFrame como un archivo CSV
df.to_csv('dataset_calificaciones.csv', index=False)

