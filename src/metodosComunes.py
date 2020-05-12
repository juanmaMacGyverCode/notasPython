def verificadorSoloNumero(dato):
    while not dato.isnumeric():
        dato = input(textoMostrar(5))
    return dato

def verificadorLongitud(numeroTexto, dato, maximo):
    while len(dato) < 3 or len(dato) > maximo:
        dato = input(textoMostrar(numeroTexto))
    return dato


def verificadorHayNumeroLongitud(numeroTexto, dato):
    hayNumero = verificadorNumero(dato)
    while len(dato) < 3 or len(dato) > 20 or hayNumero:
        dato = input(textoMostrar(numeroTexto))
        if len(dato) >= 3:
            hayNumero = verificadorNumero(dato.split(""))
    return dato


def textoMostrar(numeroTexto):
    if numeroTexto == 0:
        return "Indique de nuevo tu nombre, minimo 3 caracteres y máximo 20 caracteres y sin números: "
    elif numeroTexto == 1:
        return "Indique de nuevo tus apellidos, minimo 3 caracteres y máximo 20 caracteres y sin números: "
    elif numeroTexto == 2:
        return "Indique de nuevo tu usuario, minimo 3 caracteres y máximo 20 caracteres y sin números: "
    elif numeroTexto == 3:
        return "Indique de nuevo la contraseña, minimo 3 caracteres y máximo 20 caracteres: "
    elif numeroTexto == 4:
        return "Indique de nuevo la nota, minimo 3 caracteres y máximo 200 caracteres: "
    elif numeroTexto == 5:
        return "Indique de nuevo el codigo de la nota, solo numeros: "


def codigosErrores(codigoError):
    if codigoError == "01":
        return "Error 01!!! Todos los campos no han sido rellenados"


def verificadorNumero(datoList):

    for caracter in datoList:
        if caracter.isnumeric():
            return True
    return False
