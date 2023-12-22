cadena1 = "Soy Luigui"
cadena2 = "Working.. zZz"

#DEVUELVE TODOS LOS ATRIBUTOS DE UN OBJETO ESPECIFICADO dir(nombre_objeto) funcion de python NO metodo
toda_modificacion = dir(cadena1) 



#método que convierte a mayuscula---- METODO SE TRABAJA DE FORMA QUE -> nomb_variable.metodo()
mayuss = cadena1.upper()
mayus = "tururu".upper()
#método que convierte a minuscula
minusc = cadena2.lower()
minus = "tururu".lower()
#metodo convierte primera letra mayuscula
prim_letr_mayus = cadena1.capitalize()



#buscamos una cadena en otra cadena
busqueda_find = cadena2.find("k")
#buscamos cadena en otra cadena, sino hay coincidencias devuelve una excepción
#busqueda_index = cadena1.index("u")



#numerico =  true sino = false
es_numerico = cadena1.isnumeric()
#alfanumerio = true sino = false
es_alfanumerico = cadena1.isalpha() #valido sin espacio, de a - z es alfanumerico



#buscamos una coincidencia en otra cadena, devuelve la cantidad de veces que coincida, letra/palabra/etc...
contar_coincidencias = cadena1.count("u")
#contamos la cantidad de caracteres que posee una cadena (funcion) -> nombre_funcion(nombre_variable)
contador_caracteres = len(cadena1)
#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena2.startswith("W")
#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena2.endswith("z")



#reemplaza un pedazo de la cadena dada por otra dada
cadena_nueva = cadena2.replace("Wor", "Fuc")

#separar cadenas con la cadena que le pasemos, devuelte una lista para verificar print(type(nomb_variable)) o por posicion print(nombre_variable[posicion])
cadena_separada = cadena2.split(" ")

print(cadena_separada)