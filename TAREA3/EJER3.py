n = int(input("Ingrese Cantidad de Alumnos: "))
alumnos = {}
notas = []

print("---------------------")
for i in range(n):
    notas.append(input("Nombre del alumno: "))
    nota = float(input("Ingrese nota: "))
    if nota > 10.5:
        alumnos[notas[i]] = nota

alumnos_ordenados = dict(sorted(alumnos.items(), key=lambda item: item[1], reverse=True))

print("---------------------")
print(f"Alumnos aprobados: {alumnos_ordenados}")