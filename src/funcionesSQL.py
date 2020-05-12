import metodosComunes
import mysql.connector
import clases

def crearConector():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="programaNotas"
    )
    return database

##########################################################
"""
    CONTROL DE USUARIOS
"""
##########################################################

def registrarUsuario(listaParametros):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    ###########
    try:
        if comprobarExisteUsuario(listaParametros[0][2], "consultaExisteUsuarioRegistro"):
            print("\n\n-------------------------------\nYa existe el usuario\n-------------------------------\n")
        else:
            cursor.executemany("INSERT INTO usuarios VALUES (null, %s, %s, %s, %s)", listaParametros)
            database.commit()
            print("\n\n-------------------------------\nInsercion realizada con exito\n-------------------------------\n")
    except:
        pass
    ###########

    cursor.close()
    database.close()


def loginUsuario(listaParametros):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    ###########
    objetoUsuario = ""
    try:
        if comprobarExisteUsuario(listaParametros[0][0], "consultaExisteUsuarioLogin"):
            print("\n\n-------------------------------\nEXISTE USUARIO\n-------------------------------\n")
            cursor.execute("SELECT * FROM usuarios")
            result = cursor.fetchall()
            objetoUsuario = realizarLogin(listaParametros)
        else:
            print("\n\n-------------------------------\nNo existe usuario o contrasenna\n-------------------------------\n")
    except:
        pass
    ###########

    cursor.close()
    database.close()

    return objetoUsuario

##########################################################
"""
    GESTIÓN DE NOTAS
"""
##########################################################

def registrarNota(nota, objetoUsuario):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    ###########
    try:
        cursor.execute("INSERT INTO notas VALUES (null, '" + nota + "', " + str(objetoUsuario.getIdentificador()) + ")")
        database.commit()
    except:
        ### HACER UN LOG DE ERRORES
        print("\n\n-------------------------------\nHAY ERRORES\n-------------------------------\n")
    else:
        print("\n\n-------------------------------\nInsercion realizada con exito\n-------------------------------\n")
    ###########

    cursor.close()
    database.close()


def borrarNota(codigoNota, objetoUsuario):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    ###########
    try:
        cursor.execute("DELETE FROM notas WHERE id=" + codigoNota + " and codigoUsuario=" + str(objetoUsuario.getIdentificador()) + ";")
        database.commit()
    except:
        ### HACER UN LOG DE ERRORES
        print("\n\n-------------------------------\nHAY ERRORES\n-------------------------------\n")
    else:
        print("\n\n-------------------------------\nBorrado realizado con exito\n-------------------------------\n")
    ###########

    cursor.close()
    database.close()


def consultaNotas(objetoUsuario):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    ###########
    listaNotas = []

    try:
        cursor.execute("SELECT * FROM notas WHERE codigoUsuario=" + str(objetoUsuario.getIdentificador()) + "")
        listaNotas = cursor.fetchall()
    except:
        ### HACER UN LOG DE ERRORES
        print("\n\n-------------------------------\nHAY ERRORES\n-------------------------------\n")
    else:
        print("\n\n-------------------------------\nConsulta realizada con exito\n-------------------------------\n")
    ###########

    cursor.close()
    database.close()

    return listaNotas


##########################################################
"""
    METODOS COMUNES
"""
##########################################################

def comprobarExisteUsuario(usuarioComprobar, consulta):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    existe = False

    cursor.execute(consultaSQL(usuarioComprobar, consulta))
    usuario = cursor.fetchone()
    if usuario != None:
        if usuario[0] == usuarioComprobar:
            existe = True

    cursor.close()
    database.close()

    return existe

def consultaSQL(usuarioComprobar, consulta):
    if consulta == "consultaExisteUsuarioRegistro":
        return "SELECT usuario FROM usuarios WHERE usuario LIKE '" + usuarioComprobar + "';"
    elif consulta == "consultaExisteUsuarioLogin":
        return "SELECT usuario FROM usuarios WHERE usuario LIKE '" + usuarioComprobar + "';"

def realizarLogin(listaParametros):
    database = crearConector()
    cursor = database.cursor(buffered=True)
    cursor.execute("USE programaNotas")

    #######
    cursor.execute("SELECT * FROM usuarios WHERE usuario LIKE '" + listaParametros[0][0] + "' AND contrasenna LIKE '" + listaParametros[0][1] + "';")
    usuario = cursor.fetchone()
    if usuario != None:
        objetoUsuario = clases.Usuario(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4])
    #######

    cursor.close()
    database.close()

    return objetoUsuario
