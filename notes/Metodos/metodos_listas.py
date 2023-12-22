lista = list(["hola", "mamawebo", 54, True]) #no se suele usar pero sirve con list()
lista2 = list([False, True, 54, True, 9999])
lista3 = list([1,98,453,2,8,8])

print("Lista: ", lista)
print("Lista2: ", lista2)
print("Lista3: ", lista3)
print("")

#devuelve cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista, por separado
lista.append("glugluglu")

#agregando un elemento a lista en un indice especifico
lista.insert(1, "que ricii")

#agregando varios elementos a la lista, al la ultima posicion, elementos juntos
lista.extend([False,2039])

#eliminando un elemento de lista por indice(posicion)
lista.pop(1)

#eliminando un ultimo elemento de lista por indice(posicion)
lista.pop(-1) #(-2) anteultimo (-2+n) y asi consecutivamente

#eliminando un elemento de lista por su valor
lista.remove("mamawebo")

#elimina todos los eleemntos de la lista
#lista.clear()

#ordena la cadena de texto o lista de forma ascendente (si usamos el parametro reverse = true lo ordena en reversa)
lista3.sort()

#inviertiendo el orden de los elementos de una lista
lista3.reverse()


#DEVUELVE TODOS LOS ATRIBUTOS DE UNA TUPLA dir(("nombre_objeto")) funcion de python NO metodo
#unicamente aplicar index y count ya que no puede ser modificable
#print(dir(("djkdnkvk")))


#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(54)


print(lista3)