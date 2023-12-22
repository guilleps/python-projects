#if condicion(true):
    #accion se ejecuta
    #...
    
#if condicion(false):
    #accion no se ejecuta
    #...
    
usuario_admin = "Guillermo"
usuario_detectado = "guillermo"
if usuario_admin == usuario_detectado:
    print("Bienvenido, bruh")
else:
    print("Alerta. Desconocido detectado!!!")