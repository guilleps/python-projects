import math
num_notas = int(input("¿De cuantos alumnos va a ingresar notas?: "))
notas = []


for i in range(0, num_notas):
  nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
  notas.append(nota)
	
menor = min(notas)
mayor = max(notas)
media = sum(notas) / len(notas)
suma_cuadrados_diff = sum((x - media) ** 2 for x in notas)
desviacion_tipica = (suma_cuadrados_diff / len(notas)) ** 0.5
print(f"La menor nota es: {menor}")
print(f"La mayor nota es: {mayor}")
print(f"La media es: {media}")
print(f"La desviación típica es: {desviacion_tipica}")

