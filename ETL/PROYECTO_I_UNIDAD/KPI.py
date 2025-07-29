import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y crear DataFrame
df = pd.read_csv('C:/workspace/Python/PROYECTO/datos/AB_NYC_2019.csv', sep=',')
#print(df)

# ---------------------AUDITORIA DE DATOS----------------------

# METRICA: RELACIÓN DE DATOS A ERRORES(CANTIDAD DE DATOS CORREGIDOS)
missingValues = df.isna()
num_missing = missingValues.values.sum()
metrica_1 = (1 - (num_missing/len(df))) * 100
print(metrica_1)
print("")

# DIMENSIÓN DE INTEGRIDAD
total_elementos_incompletos = df.isnull().values.sum()
total_elementos = df.size
dimension_integridad = (1 - (total_elementos_incompletos/total_elementos)) * 100
print(dimension_integridad)

# DIMENSIÓN DE CONSISTENCIA
# POR VER QUIZA NOCHES MINIMAS ----
