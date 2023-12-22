import pandas as pd

df = pd.read_csv('C:/workspace/Python/TAREA3/csv_tarea3/cotizacion.csv')

resumen = df.describe().loc[['min', 'max', 'mean']]
resumen.index = ["MÍNIMO", "MÁXIMO", "MEDIA"]

print("COTIZACIONES IBEX35")
print("RESULTADOS POR COLUMNA")
print(resumen.to_string(header=False))