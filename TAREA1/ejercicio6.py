
peso = input("Ingrese peso (kg): ")
estatura = input("Ingrese estatura (m): ")

# round funcion para redondear
# indica primero el numero y luego los decimales máximos round(numero,max.decimales)
imc = round(float(peso)/float(estatura)**2,2)

print(imc)