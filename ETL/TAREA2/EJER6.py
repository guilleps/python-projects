n = int(input("Ingrese Cantidad de Asignaturas: "))
asignaturas = {}
cursos = []

print("---------------------")
for i in range(n):
    cursos.append(input("Nombre de la Asignatura: "))
    nota = float(input("Ingrese nota: "))
    if nota<10.5:
        asignaturas[cursos[i]] = nota
    #notas.append(int(input("Ingrese nota: ")))

print("---------------------")
print(f"Asignaturas a repetir por el estudiante: {asignaturas}")

