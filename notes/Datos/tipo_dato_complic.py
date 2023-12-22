#LISTA->Conjunto DE DATOS TIPO TEXTO llamada MATRIZ (modificable)
lista = ["Guillermo", "programing", True, 1.73] #datos de 0 al infinito

#MODIFICAR POR POSICION
lista[1] = "gaming"

#MUESTRA lista ENTERA
#print(lista)

#MUESTRA DATO POR POSICION print(matriz_nombre[posicion])
#print(lista[1])

#TUPLA -> conjunto DE DATOS TIPO TEXTO (no modificable)
#tupla = ("Guillermo", "programing", True, 1.73)
#tupla[0] = "Lucie"
#print(tupla)

#creacion conjunto (set) no imprime por posicion(indice)
#no existen datos duplicados, de lo contrario será solo uno
conjunto = {"Guillermo", "programing", True, 1.73}
#print(conjunto[2] -> no se accede al elemento)
#print(conjunto)

#creando un diccionario -> (dict) es busqueda por nombre del dato y no por posicion de 0 a más 
diccionario = { 
    #'key' : "value", 
    'nombre' : "Guillermo", #0
    'cargo' : "programing", #1
    'working' : True, #2
    'altura' : 1.73, #3
    'dato_duplicado' : "programing" #4
}
print(diccionario) #llama a todo el diccionario
print(diccionario['nombre']) #llama a un dato especifico -> por nombre correspondiente