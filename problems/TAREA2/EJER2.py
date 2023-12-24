n = int(input("Ingrese Cantidad de asignaturas a registrar: "))
asignaturas = []

print("---------------------")
for i in range(0,n):
    asignaturas.append(input("Nombre de la Asignatura: "))
print("---------------------")


for asignatura in asignaturas:
    print(f"Yo estudio {asignatura}")