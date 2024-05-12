n = int(input("Ingrese Numeros Ganadores a ingresar: "))
numeros= []

print("---------------------")
for i in range(0,n):
   numeros.append(int(input("Ingrese número: ")))
print("---------------------")

numeros.sort()

print("Números ganadores ordenados de menor a mayor:")
for numero in numeros:
    print(numero)