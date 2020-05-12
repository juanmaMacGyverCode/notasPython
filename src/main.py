import funciones

accion = funciones.elegirRegistroLogin().lower()
while accion != "salir":
    if accion == "registro":
        funciones.formularioRegistro()
    elif accion == "login":
        funciones.formularioLogin()
    accion = funciones.elegirRegistroLogin().lower()
        
print("Adios")
