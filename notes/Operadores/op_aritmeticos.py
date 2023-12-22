#suma y resta (+ y -)
suma = 12 + 5
resta = 12 - 5


#multiplicacion y divison (* y /)
multi = 12 * 5
div = 12 / 5 #imprime dato_tipo -> float

#potenciacion (exponente) (**)
exponente = 12**5

#division_baja (//)
division_baja = 12//5 #devuelve valor redondeado menor de .5 numero menor, mayor o igual a .5 numero mayor

#resto o modulo (%)
resto = 12 % 5

#type() devuelve tipo de dato correspondiente
tipo_de_Dato = type(div) 
print(tipo_de_Dato)

#print(div)


n1 = int(input("Ingrese numero1: "))
n2 = input("Ingrese numero2: ")
n2 = int(n2)
media = (n1 + n2) / 2
print("La media resultado de {n1} y {n2} es...", media)