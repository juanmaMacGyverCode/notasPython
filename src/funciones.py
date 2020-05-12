import funcionesSQL
import metodosComunes
import clases

##########################################################
"""
    PANTALLA REGISTRO LOGIN O SALIR
"""
##########################################################

def elegirRegistroLogin():
    dato = input("Que accion desea realizar?: \n - Registro \n - Login \n - Salir \n")
    while dato.lower() != "registro" and dato.lower() != "login" and dato.lower() != "salir":
        dato = input("Indique de nuevo. \nQue accion desea realizar?: \n - Registro \n - Login \n - Salir \n")
    return dato

##########################################################
"""
    REGISTRO
"""
##########################################################

def formularioRegistro():
    print("\n\n-------------------------------\nFormulario de registro\n-------------------------------\n")

    dato = input("Cual es tu nombre?: ")
    nombre = metodosComunes.verificadorHayNumeroLongitud(0, dato)

    dato = input("Cuales son tus apellidos?: ")
    apellidos = metodosComunes.verificadorHayNumeroLongitud(1, dato)

    dato = input("Escribe tu nombre de usuario: ")
    nombreUsuario = metodosComunes.verificadorHayNumeroLongitud(2, dato)

    dato = input("Escribe la contrasenna: ")
    contrasenna = metodosComunes.verificadorLongitud(3, dato, 20)

    if nombre != None and apellidos != None and nombreUsuario != None and contrasenna != None:
        listaParametros = [(nombre, apellidos, nombreUsuario, contrasenna)]
        funcionesSQL.registrarUsuario(listaParametros)
    else:
        print(metodosComunes.codigosErrores("01"))


##########################################################
"""
    LOGIN
"""
##########################################################

def formularioLogin():
    print("\n\n-------------------------------\nFormulario de login\n-------------------------------\n")

    dato = input("Escribe tu nombre de usuario: ")
    nombreUsuario = metodosComunes.verificadorHayNumeroLongitud(2, dato)

    dato = input("Escribe la contrasenna: ")
    contrasenna = metodosComunes.verificadorLongitud(3, dato, 20)

    if nombreUsuario != None and contrasenna != None:
        listaParametros = [(nombreUsuario, contrasenna)]
        objetoUsuario = funcionesSQL.loginUsuario(listaParametros)
        print("Has iniciado sesion con el usuario: " + objetoUsuario.getUsuario())
        menuProgramaNotas(objetoUsuario)
    else:
        print(metodosComunes.codigosErrores("01"))

def menuProgramaNotas(objetoUsuario):

    accion = elegirMenuProgramaNotas().lower()
    while accion != "salir":
        if accion == "crear":
            print("\n\n-------------------------------\nCREAR NOTA\n-------------------------------\n")
            crearNota(objetoUsuario)
        elif accion == "borrar":
            print("\n\n-------------------------------\nBORRAR NOTA\n-------------------------------\n")
            borrarUnaNota(objetoUsuario)
        elif accion == "consultar":
            print("\n\n-------------------------------\nCONSULTAR NOTAS\n-------------------------------\n")
            consultarTodasLasNotas(objetoUsuario)
        accion = elegirMenuProgramaNotas().lower()
    
    print("Cerrando sesion de " + objetoUsuario.getNombre())

def elegirMenuProgramaNotas():
    dato = input("\n\n-------------------------------\nQue accion desea realizar?: \n - Crear nota (crear) \n - Borrar nota (borrar) \n - Consultar notas (consultar) \n - Salir \n-------------------------------\n")
    while dato.lower() != "crear" and dato.lower() != "borrar" and dato.lower() != "consultar" and dato.lower() != "salir":
        dato = input("\n\n-------------------------------\nIndique de nuevo. \nQue accion desea realizar?: \n - Crear nota (crear) \n - Borrar nota (borrar) \n - Consultar notas (consultar) \n - Salir \n-------------------------------\n")
    return dato

##########################################################
"""
    CREAR NOTA
"""
##########################################################

def crearNota(objetoUsuario):
    dato = input("Que nota desea escribir?: ")
    nota = metodosComunes.verificadorLongitud(4, dato, 200)

    if nota != None:
        funcionesSQL.registrarNota(nota, objetoUsuario)
    else:
        print(metodosComunes.codigosErrores("01"))


##########################################################
"""
    BORRAR NOTA
"""
##########################################################

def borrarUnaNota(objetoUsuario):
    dato = input("Que nota desea borar? Indique su codigo: ")
    codigoNota = metodosComunes.verificadorSoloNumero(dato)

    if codigoNota != None:
        funcionesSQL.borrarNota(codigoNota, objetoUsuario)
    else:
        print(metodosComunes.codigosErrores("01"))

##########################################################
"""
    CONSULTAR TODAS LAS NOTAS
"""
##########################################################

def consultarTodasLasNotas(objetoUsuario):
    listaNotas = funcionesSQL.consultaNotas(objetoUsuario)

    for consultandoNota in listaNotas:
        print("----------------------------------")
        print(f"Codigo de la nota: {consultandoNota[0]}")
        print(f"Nota: {consultandoNota[1]}")
        print(f"Codigo del usuario: {consultandoNota[2]}")
        print("\n")


