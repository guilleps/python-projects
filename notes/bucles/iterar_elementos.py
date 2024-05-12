animales = ["gato","perro","loro","cocodrilo"]
numeros = [1,59,45,23]

#recorriendo lista animales
for animal in animales:
    print(f"Pasando por... {animal}")
    
#recorriendo lista numeros y multiplicando cada uno por 10
for numero in numeros:
    print(f"Pasando por... {numero * 10}")
    
#recorriendo varias listas: iterando al mismo tiempo, del mismo tamaño
for animal,numero in zip(animales,numeros):
    print(f"Pasando por numero... {numero}")
    print(f"Pasando por animal... {animal}")
    

#recorre numeros en range(numero_inicial,numero_final)
for num in range(5,10):
    print(num)
    
#forma no optima de recorrer una listas (NO FUNFIONA EN CONJUNTOS)
for num in range(len(numeros)):
    print(numeros[num])
    
    
#forma correcta de recorrer una lista con indice -> enumerate()
for num,i in enumerate(numeros):
    print(f"En la posicion {num}, el valor es {i}")
    
    
#usando el for/else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
#else siempre se ejecuta
else:
    print("el bucle terminó")
    
    
#funciona exactmente igual en tuplas, listas y conjuntos