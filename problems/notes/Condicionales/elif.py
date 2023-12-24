ingreso_mensual = 15000
gasto_diario = 14000


#if anidados y else if (elif)
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_diario < 0:
        print("Estado: Deficit dineral")
        
    elif ingreso_mensual - gasto_diario > 3000:
        print("ahorra pa la chamba")
        
    else:
        print("ta bien")
            
elif ingreso_mensual > 1000:
    print("Sostenible solo en LATAM")

elif ingreso_mensual > 500:
    print("Sostenible para un individuo")
    
elif ingreso_mensual > 100:
    print("Ni para el chicle causa")