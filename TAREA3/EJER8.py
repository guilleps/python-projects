import numpy as np
import datetime as dt

import pandas as pd

emisiones_2016 = pd.read_csv('C:/workspace/Python/TAREA3/csv_tarea3/emisiones-2016.csv', sep = ';')
emisiones_2017 = pd.read_csv('C:/workspace/Python/TAREA3/csv_tarea3/emisiones-2017.csv', sep = ';')
emisiones_2018 = pd.read_csv('C:/workspace/Python/TAREA3/csv_tarea3/emisiones-2018.csv', sep = ';')
emisiones_2019 = pd.read_csv('C:/workspace/Python/TAREA3/csv_tarea3/emisiones-2019.csv', sep = ';')

emisiones = pd.concat([emisiones_2016, emisiones_2017, emisiones_2018, emisiones_2019])
print(emisiones)

columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
columnas.extend([col for col in emisiones if col.startswith('D')])
emisiones = emisiones[columnas]
print(emisiones)

emisiones = emisiones.melt(id_vars= ['ESTACION', 'MAGNITUD', 'ANO', 'MES'], var_name = 'DIA', value_name = 'VALOR')
print(emisiones)

emisiones['FECHA'] = emisiones.ANO.apply(str) + '/' + emisiones.MES.apply(str) + '/' + emisiones.DIA.apply(str)
print(emisiones)

emisiones.sort_values(['ESTACION', 'MAGNITUD', 'FECHA'])
print(emisiones)

emisiones.groupby(['ESTACION', 'MAGNITUD']).VALOR.describe()
print(emisiones)

def evolucion_mensual(contaminante, año):
    return emisiones[(emisiones.MAGNITUD == contaminante) & (emisiones.ANO == año)].groupby(['ESTACION', 'MES']).VALOR.mean().unstack('MES')
evolucion_mensual(8, 2019)

def resumen(estacion, contaminante):
    return emisiones[(emisiones.ESTACION == estacion) & (emisiones.MAGNITUD == contaminante)].VALOR.describe()
print(f"Resumen del dióxido de nitrógeno en plaza elíptica: {resumen(56, 8)}")
print(f"Resumen del dióxido de nitrógeno en plaza del carmen: {resumen(35, 8)}")

emisiones.groupby('MAGNITUD').VALOR.describe()

def media_mensual(estacion):
    return emisiones[(emisiones.ESTACION == estacion)].groupby(['MAGNITUD', 'MES']).VALOR.mean().unstack('MES')
media_mensual(56)

