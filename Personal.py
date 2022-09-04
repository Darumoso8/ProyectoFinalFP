class Personal:

    """La clase Personal crea y define un trabajador dentro de la 
    veterinaria
    
    Los datos almacenados para cada trabajador son: nombre (str),
    correro electronico (str) y su número de telefono (str)
     """

    def __init__(self:object, nombre:str, correo:str,
                numeroDeTelefono:str) -> None:
        self.nombre = nombre
        self.correo = correo
        self.numeroDeTelefono = numeroDeTelefono
    
    def registrar(self:object, registo:list) -> None:
        pass


class PersonalMedico(Personal):
    """La clase PersonalMedico es una subclase de Personal, tiene como
    atributo extra la especialidad del médico(str)"""

    def __init__(self:object, nombre:str, correo:str,
                numeroDeTelefono:str, especialidad:str) -> None:
        super().__init__(nombre, correo, numeroDeTelefono)
        self.especialidad = especialidad

    def registrar(self: object, registo: list) -> None:
        """El método registrar almacena los nombres del personal
        médico en una lista"""
        registo.append(self.nombre)


class PersonalAdministrativo(Personal):
    """La clase PersonalAdmnistrativo hereda de Personal, tiene como
    atributo extra la contraseña (str) para el inicio de sesión"""

    def __init__(self:object, nombre:str, correo:str,
                numeroDeTelefono:str, contrasena:str) -> None:
        super().__init__(nombre, correo, numeroDeTelefono)
        self.__contrasena = contrasena
    
    def registrar(self: object, registo: list) -> None:
        """El método registrar almacena los nombres del personal
        administrativo en una lista"""
        registo.append(self.nombre)

    @property
    def contrasena(self:object) -> str:
        return self.__contrasena

    @contrasena.setter
    def contrasena(self:object, nuevaContrasena:str) -> None:
        self.__contrasena = nuevaContrasena

    @contrasena.deleter
    def contrasena(self:object) -> None:
        del self.__contrasena

     

    


        
        





