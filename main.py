"""
El programa será un sistema para llevar un control del inventario
y ventas de una tienda de mascotas. 

Se van a considerar todos los productos y bienes que se encuentran
en una veterinaria, así como tambien llevar un control en el
área de gestión de la misma.

Dentro de los bienes se considera todo aquel producto que pueda ser
vendido y almacenado, como servicios se consideran servicios médicos
y servicios de estética.

En la parte de gestión se lleva un control sobre el personal, 
tanto personal administrativo como el personal médico

"""

from Producto import *
from Personal import *

#Llenado de datos provisional
codigoDeBarras = input("Codigo de barras: ")
nombre = input("Nombre: ")
marca = input("Marca: ")
precio = input("Precio")
cantidadEnAlmacen = input("Cantidad en almacén: ")

try:
    int(precio)
    int(cantidadEnAlmacen)
except ValueError:
    print("ERROR! El precio y la cantidad en almacen deben ser enteros")

ejemplo1 = Producto(codigoDeBarras, nombre, marca, precio, cantidadEnAlmacen)


print(ejemplo1.descripcion())
print(ejemplo1.darNombre())
print(ejemplo1.darMarca())
print(ejemplo1.darPrecio())
print(ejemplo1._cantidadEnAlmacen)



ejemplo2 = PersonalAdministrativo("Juan Ramirez", "correo@dominio.com",
                                    "5588032873", "password1234")

print(ejemplo2.contrasena)
ejemplo2.contrasena = "4723"
print(ejemplo2.contrasena)
del ejemplo2.contrasena

try:
   print("La contrasena es: ", ejemplo2.contrasena)
except AttributeError:
    print("La contraseña ya no existe")



