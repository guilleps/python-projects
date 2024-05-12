print("Dime una oración")
oracion = input("Aquí: ")


#Cuenta caracteres de una oracion/frase
contador_caracteres = len(oracion)


#Cuenta cuantos elementos hay en una frase/oracion
separa_oracion_palabras = oracion.split(" ")
contador_palabras = len(separa_oracion_palabras)

print("---------------------")
print(oracion.upper())
print("---------------------")
print(f"En la oración dada se contaron... {contador_caracteres} caracteres")
print("---------------------")
print(f"Proceso -> separacionde elementos... {separa_oracion_palabras}")
print(f"Se contaron {contador_palabras} palabras y tardarias {contador_palabras/2} segundos en decirlo")
print("---------------------")
print(f"El yutuber Dalto se tardaria {contador_palabras * 100 // 2 * 1.3 / 100} segundos en decirlo")

print("---------------------")
if contador_palabras > 120:
    print("WACHO CALMATE UN RATO")