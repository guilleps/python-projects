

inversion = int(input("Ingrese inversion: "))
interes_anual = int(input("Ingres interes anual: "))
anios = int(input("Ingres numero de años: "))


capital = inversion/((interes_anual/100+1)*anios)

print(capital)

