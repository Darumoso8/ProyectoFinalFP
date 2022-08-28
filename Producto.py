class Producto:
    """
    La clase Producto crea y define un producto
    
    Usa el codigoDeBarras (str), como llave de un diccionario donde
    almacena los valores de nombre (str), marca (str), precio (int)
    y cantidad en el almacén (int) 
    """

    def __init__(self:object, codigoDeBarras:str, nombre:str, 
                marca:str, precio:int, cantidadEnAlmacen:int) -> None:
        """
        El método constructor de Producto almacena los valores de 
        codigoDeBarras y cantidadEnAlmacen como atributos, además los
        valores de nombre, marca y precio se almacenan en una lista
        a la que se le asignará una llave, de esta forma creando el 
        atributo caracteristicas (dict)
        """

        self.codigoDeBarras = codigoDeBarras       
        self._cantidadEnAlmacen = cantidadEnAlmacen
        self.caracteristicas = dict()
        valores = []
        valores.extend([nombre, marca, 
                        precio])  
        self.caracteristicas[self.codigoDeBarras] = valores


    def descripcion(self) -> dict:
        return self.caracteristicas

    """
    Las funciones definidas como darNombre, darMarca y dar Precio
    retornan el atributo solicitado a partir de la llave y de su 
    lugar en la lista de valores
    """

    def darNombre(self:object) -> str:
        return self.caracteristicas[self.codigoDeBarras][0]
        
    def darMarca(self:object) -> str:
        return self.caracteristicas[self.codigoDeBarras][1]

    def darPrecio(self:object) -> int:
        return self.caracteristicas[self.codigoDeBarras][2]        

