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

from pickletools import read_int4
from Producto import *
from Personal import *
from conexion import *

def validarEntero(x):
    try:
        num = int(x)
        return num
    except:
        print("ERROR! Ingrese un numero") 

inicializarTabla()
inicializarTablaPersonalMedico()
almacen = recopilarDatos()
medicos = recopilarMedicos()

#usuario = input("Para iniciar sesión ingrese su usuario: ")
#contrasena = input("Ingrese su contraseña: ")

while True:
    print("1- Agregar medico")
    print("2- Dar de baja a un medico")
    print("3- Dar informacion de algun medico")
    print("4- Ver medicos")
    opcion = input("Eliga su opcion: ")

    if opcion == '1':
        curp = input("Ingrese el curp: ")
        nombre = input("Ingrese el nombre: ")
        correo = input("Ingrese la correo: ")
        numeroDeTelefono = input("Ingrese el numero de telefono: ")
        especialidad = input("Ingrese la especialidad: ")
        registrarNuevoMedico(curp, nombre, correo, numeroDeTelefono, especialidad)
        medicos = recopilarMedicos()
        break
    
    if opcion == '2':
        curp = input("Ingrese el curp del medico a dar de baja: ")
        darDeBajaMedico(curp, medicos)
        medicos = recopilarMedicos

    if opcion == '3':
        curp = input("Ingrese el curp del medico que quiera revisar: ")
        for i in medicos:
            if i["curp"] == curp:
                print(i)
            else:
                [print("Ese curp no existe, intenta de nuevo")]

    if opcion == '4':
        for i in medicos:
            print(i)






"""
while True:
    print("1- Agregar producto")
    print("2- Vender producto")
    print("3- Comprar producto")
    print("4- Comprobar existencia de producto")
    print("5- Ver almacen")
    opcion = input("Eliga su opcion: ")

    if opcion == '1':
        nombre = input("Ingrese el nombre: ")
        marca = input("Ingrese la marca: ")
        precio = validarEntero(input("Ingrese el precio: "))
        cantidad = validarEntero(input("Ingrese la cantidad: "))
        agregarProductos(nombre, marca, precio, cantidad)
        almacen = recopilarDatos()

    elif opcion == '2':
        codigo = input("Ingrese el codigo de barras: ")
        cantidad = validarEntero(input("Ingrese cantidad: "))
        if cantidad <= 0:
            print("ERROR! Ingrese valores válidos")
            continue
        venderProducto(codigo, almacen, cantidad)
        almacen = recopilarDatos()

    elif opcion == '3':
        codigo = input("Ingrese el codigo de barras: ")
        cantidad = validarEntero(input("Ingrese cantidad: "))
        if cantidad <= 0:
            print("ERROR! Ingrese valores válidos")
            continue
        comprarProducto(codigo, almacen, cantidad)
        almacen = recopilarDatos()

    elif opcion == '4':
        codigo = input("Ingrese el código de barras que quiera comprobar: ")
        for i in almacen:
            if i["codigoDeBarras"] == codigo:
                print(f'Hay {i["_cantidadEnAlmacen"]} {i.darNombre()} de la marca {i.darMarca()} en el almacen')

    elif opcion == '5':
        for i in almacen: 
            print(i.descripcion())
"""








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
