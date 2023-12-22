#creando diccionarios con dict()
diccionario = dict(nombre="guillermo",apellido="palacios")

#las litsas no pueden ser claves y usamos frozenset() para meter conjuntos
diccionario = {frozenset(["amigo","mio"]):"guau"}

#creando diciconarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido","objetivo"])
#print(diccionario["nombre"])

print(diccionario)