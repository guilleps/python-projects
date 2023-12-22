abecedario = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

multiplos = []

print(f"Abecedario original:")
print(abecedario)

for i, letra in enumerate(abecedario):
    if (i + 1) % 3 != 0:
        multiplos.append(letra)

print("---------------------------")
print("Abecedario sin múltiplos de 3:")
print(multiplos)