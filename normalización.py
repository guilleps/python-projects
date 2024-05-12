# # NORMALIZACION
# for n in range(1, 101):
#     normalizacion = (n - 1) / (100 - 1)
#     print(normalizacion)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lee el archivo CSV y crear DataFrame
data_set = pd.read_csv('C:/workspace/Python/PROYECTO/datos/AB_NYC_2019.csv', sep=',')

Q1 = data_set["price"].quantile(0.25) # cuartil 1
print(f"Cuartil 1 = {Q1}")

Q3 = data_set["price"].quantile(0.75) # cuartil 3
print(f"Cuartil 3 = {Q3}")

IQR = Q3 - Q1 # rango intercuartil
print(f"Rango intercuartil = {IQR}")

Mediana = data_set["price"].median() # mediana
print(f"Mediana de precios = {Mediana}")

Valor_mínimo = data_set["price"].min() # mínimo
print(f"Valor minimo de precios = {Valor_mínimo}")

Valor_máximo = data_set["price"].max() # máximo
print(f"Valor maximo de precios = {Valor_máximo}")

Bi = (Q1-1.5*IQR) # bigote inferior
print(f"Bigote inferior = {Bi}")

Bs= (Q3*1.5*IQR) # bigote superior
print(f"Bigote superior = {Bs}")

Ubicación_outliers=(data_set["price"] < Bi) | (data_set["price"] > Bs) # oper. OR
print(Ubicación_outliers)

Outliers = data_set[Ubicación_outliers]
print(Outliers)

Ubicación_sin_out = (data_set["price"] >= Bi) & (data_set["price"] <= Bs) # oper. AND
print(Ubicación_sin_out)

Sin_outliers = data_set[Ubicación_sin_out]
print(Sin_outliers)


