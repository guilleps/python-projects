n = int(input("Ingrese Cantidad de números: "))
numeros = []

print("---------------------")
for i in range(0,n):
   numeros.append(int(input("Ingrese número: ")))
print("---------------------")

suma = sum(numeros)

media = suma/len(numeros)

print(f"La media de los números ingresados es: {media}")

suma_cuadrados_diferencias = sum((x - media) ** 2 for x in numeros)

desviacion_tipica = (suma_cuadrados_diferencias / len(numeros)) ** 0.5

print(f"La desviación típica de los números ingresados es: {desviacion_tipica}")