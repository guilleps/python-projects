import pandas as pd

datos = pd.DataFrame({
    "Mes": ["Enero","Febrero","Marzo","Abril"],
    "Ventas": [30500, 35600, 28300, 33900],
    "Gastos": [22000, 23400, 18100, 20700]
})

print(datos)
    
balance_total = datos["Ventas"].sum() - datos["Gastos"].sum()

print(f"\nEl balance total en los meses seleccionados es: {balance_total}")