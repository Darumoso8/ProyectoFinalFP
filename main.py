"""
El programa será un sistema para llevar un control del inventario
y ventas de una tienda de mascotas. 

Se van a considerar todos los productos y bienes que se encuentran
en una veterinaria, así como tambien llevar un control en el
área de gestión de la misma.

La nomenclatura para los códigos de barra es: NNMMPP, donde NN son
las dos primeras letras del nombre, MM las dos primeras letras de la 
marca y PP los dos primeros dígitos del precio (En caso de ser 
unidigital se pone un 0 antes)

Dentro de los bienes se considera todo aquel producto que pueda ser
vendido y almacenado, como servicios se consideran servicios médicos
y servicios de estética.

En la parte de gestión se lleva un control sobre el personal, 
tanto personal administrativo como el personal médico

"""

from Producto import *
from Personal import *
from conexion import *

inicializarTabla()
almacen = recopilarDatos()

while True:
    print("1- Agregar producto")
    print("2- Vender producto")
    print("3- Combrobar existencia de producto")
    print("4- Ver almacen")
    opcion = input("Eliga su opcion: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre: ")
        marca = input("Ingrese la marca: ")
        precio = int(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
        agregarProductos(nombre, marca, precio, cantidad)
        almacen = recopilarDatos()

    elif opcion == '2':
        codigo = input("Ingrese el codigo de barras: ")
        cantidad = input("Ingrese cantidad: ")
        venderProducto(codigo, almacen, cantidad)
        almacen = recopilarDatos()

    elif opcion == '3':
        codigo = input("Ingrese el código de barras que quiera comprobar: ")
        for i in almacen:
            if i["codigoDeBarras"] == codigo:
                print(f'Hay {i["_cantidadEnAlmacen"]} {i.darNombre()} de la marca {i.darMarca()} en el almacen')

    elif opcion == '4':
        for i in almacen: 
            print(i.descripcion())
        










# ejemplo2 = PersonalAdministrativo("Juan Ramirez", "correo@dominio.com",
#                                     "5588032873", "password1234")

# print(ejemplo2.contrasena)
# ejemplo2.contrasena = "4723"
# print(ejemplo2.contrasena)
# del ejemplo2.contrasena

# try:
#    print("La contrasena es: ", ejemplo2.contrasena)
# except AttributeError:
#     print("La contraseña ya no existe")
