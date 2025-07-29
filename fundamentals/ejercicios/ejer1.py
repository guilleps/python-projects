#promedio de duracion en horas
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

#duracion de crudos(video sin editar)
crudo_prom = 5
crudo_actual = 3.5

#diferencias de duracion 
diferencia_minima = 100 - (curso_actual / otros_cursos_min * 100)
diferencia_max = 100 - (curso_actual * 1000 // otros_cursos_max / 10)
diferencia_prom = 100 - (curso_actual / otros_cursos_promedio * 100)

#calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio = 100 - (otros_cursos_promedio * 1000 // crudo_prom / 10)
tiempo_vacio_actual = 100 - (curso_actual * 1000 // crudo_actual / 10)


#RESPUESTA A DIFERENCIAS EN PORCENTAJE DE DURACION - EJER 1
print("El curso actual dura...")
print(f"- Un {diferencia_minima}% menos que el más rapido")
print(f"- Un {diferencia_max}% menos que el más lento")
print(f"- En promedio {diferencia_prom}% menos que el promedio")

print("-----------------------------------------------------------------------------------")

#RESPUESTA DE CANTIDAD DE ESPACIO VACIO QUE SE EDITA - EJER 2
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"El cursos actual eliminó {tiempo_vacio_actual}% de tiempo vacio")

print("-----------------------------------------------------------------------------------")

#RESPUESTA DE DIFERENCIA SI DURARA 10 HORAS - EJER 3
print(f"Ver 10 horas de este curso es igual a ver {otros_cursos_promedio * 100 // curso_actual / 10} horas de otro curso")
print(f"Ver 10 horas de otros cursos es igual a ver {curso_actual * 100 // otros_cursos_promedio / 10} horas de este curso")