frutas = ["manzana","platano","uva","sandia"]
cadena = "Mama mia"
numeros = [4,35,24,1]

#evitando recorrer una fruta con sentencia continue
for fruta in frutas:
    if fruta == "platano":
        continue
    print(f"Me voy a comer una {fruta}")
    
    
#evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "manzana":
        break #aborta la ejecución
    print(f"Me voy a comer una {fruta}")

print("Error.. El bucle colapsó")


#recorre una cadena de texto
for letra in cadena:
    print(letra)
    

#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)