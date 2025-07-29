diccionario = {
    "nombre" : "luigui",
    "apellido" : "palacios",
    "objetivo" : "Senior",
    "paga" : 85000
}

#devuelve las claves(keys) y tmb sirve para iterar
#claves = diccionario.keys()

#devuelve el valor de una clave(key), en caso no obtenga valor devuelve un None(no tiene valor) no una excepcion, el programa continua
#claves = diccionario["objetivo"]
claves = diccionario.get("objetivo")

#eliminando todo el diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("objetivo")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)