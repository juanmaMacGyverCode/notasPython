class Usuario:

    __identificador = ""
    __nombre = ""
    __apellidos = ""
    __usuario = ""
    __contrasenna = ""

    def __init__(self, identificador, nombre, apellidos, usuario, contrasenna):
        self.identificador = identificador
        self.nombre = nombre
        self.apellidos = apellidos
        self.usuario = usuario
        self.contrasenna = contrasenna

    def getIdentificador(self):
        return self.identificador

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getUsuario(self):
        return self.usuario
    
    def getContrasenna(self):
        return self.contrasenna

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContrasenna(self, contrasenna):
        self.contrasenna = contrasenna
        

class Nota:

    __identificador = ""
    __nota = ""
    __usuario = ""

    def __init__(self, identificador, nota, usuario):
        self.identificador = identificador
        self.nota = nota
        self.usuario = usuario

    def getIdentificador(self):
        return self.identificador

    def getNota(self):
        return self.nota

    def getUsuario(self):
        return self.usuario

    def setIdentificador(self, identificador):
        self.identificador = identificador

    def setNota(self, nota):
        self.nota = nota

    def setUsuario(self, usuario):
        self.usuario = usuario
