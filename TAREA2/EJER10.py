vectorA = [1,2,3]
vectorB = [-1,0,2]

print(f"Coordenadas del vector A = {vectorA}")
print(f"Coordenadas del vector B = {vectorB}")

prod_esc = 0
for i in range(len(vectorA)):
    prod_esc += vectorA[i] * vectorB[i]

print(f"El producto escalar de A y B es : {prod_esc}")