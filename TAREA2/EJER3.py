n = int(input("Ingrese Cantidad de Asignaturas: "))
asignaturas = []
notas = []

print("---------------------")
for i in range(0,n):
    asignaturas.append(input("Nombre de la Asignatura: "))
    notas.append(int(input("Ingrese nota: ")))

print("---------------------")


for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
