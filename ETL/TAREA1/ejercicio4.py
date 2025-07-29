
nombre = input("Ingrese nombre del trabajador: ")
horas_trabajadas = int(input("Ingrese cantidad de horas trabajadas: "))
pago_hora = int(input("Ingrese pago x hora: "))

paga = horas_trabajadas * pago_hora

print(f"La cantidad de horas trabajadas del señor {nombre.upper()} es de: ")
print(paga," dolares")