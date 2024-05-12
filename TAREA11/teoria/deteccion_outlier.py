import numpy as np

datos = [1, 2, 2, 2, 3, 1, 1, 15, 2, 2, 2, 3, 1, 1, 2]
media = np.mean(datos)
desviacion_std = np.std(datos)
print('La media del dataset es: ', media)
print('La desviación estándar es: ', desviacion_std)
umbral = 3
outlier = []
for i in datos:
    z = (i-media)/desviacion_std
    if z > umbral:
        outlier.append(i)
print('El outlier del dataset es: ', outlier)
