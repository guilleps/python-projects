palabra = input("Ingrese una palabra: ").lower()

conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palabra:
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

for vocal, contador in conteo_vocales.items():
    print(f"Numero de veces que aparece la vocal '{vocal}': {contador}")