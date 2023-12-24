diccionario = {
    "nombre" : "guillermo",
    "grado" : "militar",
    "cargo" : "sexologo",
    "tamaño" : 16
}

#recorre key, variables_nombre
for key in diccionario:
    print(f"La clave es: {key}")
    
#recorre el diccionario con -> item() para obtner la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y el valor es: {value}")