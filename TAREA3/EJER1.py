import pandas as pd

rango_anio = int(input("Ingrese cantidad de años a registrar: "))

ventas = {}
print("---------------------")

for anio in range(0, rango_anio): 
    anio = int(input("Ingrese año: "))
    venta = float(input(f"Ingrese las ventas para el año {anio}: "))
    ventas[anio] = venta

print("---------------------")

for anio, venta in ventas.items():
    print(f"En el año {anio} se hizo una venta de {venta}")

print("---------------------")

for anio, venta in ventas.items():
    print(f"En el año {anio} se hizo una venta de {round(venta * 0.9, 2)}")
    