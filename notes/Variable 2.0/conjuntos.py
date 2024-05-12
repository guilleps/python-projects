#creando un conjunto con set()
conjunto = set(["Dato 1","Dato 2"])

#metiendo un conjunto dentro de otro conjunto con funcion -> frozenset()
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1,"dato 3"}




#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#issubset() -> verifica si es un subconjunto de...¿ retorna rpta true/false ---  (<=) tambien funciona
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#issuperset() -> verifica si es un superconjunto de...¿ retorna rpta true/false ---  (>) tambien funciona
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificando si hay algun numero en comun -> .isdisjoint()
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)