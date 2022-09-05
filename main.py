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
from os import system
from Producto import *
from Personal import *
from conexion import *

def validarEntero(x):
    '''
    Validar entero comprueba que se trate de algún valor
    entero y lo retorna ya transformado
    '''
    try:
        num = int(x)
        return num
    except:
        print("ERROR! Ingrese un numero") 

'''
En el siguiente bloque de código se llama a mandar las funciones
para inicialiar las tablas en la BD, además se recopilan los datos
de estas tablas y se guardan en lista con el nombre correspondiente
'''
inicializarTabla()
inicializarTablaPersonalMedico()
inicializarTablaPersonalAdministrativo()
almacen = recopilarDatos()
medicos = recopilarMedicos()
administrativos = recopilarAdministrativos()

while True:
    '''
    Este menú recursivo es el principal, aqui se inicia sesión (En alguna
    cuenta del personal administrativo) y tambien se sale del programa 
    '''
    usuario = input("Para iniciar sesión ingrese su curp: ")
    contrasena = input("Ingrese su contraseña: ")

    correcto = False
    for i in administrativos:
        '''
        Aqui se comprueba si los valores de usuario y contraseña están
        ligados a una cuenta administrativa, en caso de estarlo correcto 
        se vuelve true, lo que significa que se puede entrar al menú de 
        acciones
        '''
        if i.curp == usuario and i.contrasena == contrasena:
            correcto = True
            usuarioActual = i

    while correcto:
        '''
        Una vez dentro del menú de acciones se puede accedere a los
        distintos aspectos a gestionar
        '''
        system("cls")
        print("1- Menu de medicos")
        print("2- Menu de administrativos") 
        print("3- Menu de ventas")
        print("4- Cerrar Sesion") 
        opcionMenu = input("Ingrese su opcion: ")

        if opcionMenu == '1':
            system("cls")
            while True:
                '''
                En esta parte se encuentra la gestión del personal
                médico
                '''
                print("1- Dar informacion de algun medico")
                print("2- Ver medicos")
                print("3- Gestionar opciones de administrador")
                print("4- Salir")
                opcion = input("Eliga su opcion: ")

                if opcion == '1':
                    system("cls")
                    existe = False
                    curp = input("Ingrese el curp del medico que quiera revisar: ")
                    for i in medicos:
                        if i["curp"] == curp:
                            print(i, "\n")
                            existe = True
                    if not existe:        
                        print("Ese curp no existe, intenta de nuevo")

                elif opcion == '2':
                    system("cls")
                    for i in medicos:
                        print(i, "\n")

                elif (usuario == 'CURP1') and (opcion == '3'):
                    '''
                    En esta parte únicamente puede ingresar el administrador
                    principal, de esta forma cuenta con acciones extras 
                    desplegadas en otro menú
                    '''
                    system("cls")
                    print("1- Agregar medico")
                    print("2- Dar de baja a un medico")
                    print("3- Regresar")

                    opcion = input("Eliga su opcion: ")

                    if opcion == '1':
                        system("cls")
                        curp = input("Ingrese el curp: ")
                        nombre = input("Ingrese el nombre: ")
                        correo = input("Ingrese la correo: ")
                        numeroDeTelefono = input("Ingrese el numero de telefono: ")
                        especialidad = input("Ingrese la especialidad: ")
                        registrarNuevoMedico(curp, nombre, correo, numeroDeTelefono, especialidad)
                        medicos = recopilarMedicos()
                    
                    elif opcion == '2':
                        system("cls")
                        curp = input("Ingrese el curp del medico a dar de baja: ")
                        darDeBajaMedico(curp, medicos)
                        medicos = recopilarMedicos()
                    
                    elif opcion == '3':
                        break
            
                elif opcion == '4':
                    break 

                else:
                    print("No tienes permisos para esto")

        elif opcionMenu == '2':
            system("cls")
            while True:
                '''
                En esta parte se encuentra la gestión del personal
                administrativo, todo aquel que no sea el admin principal
                únicamente puede cambiar su contraseña.
                '''
                print("1- Cambiar contraseña")
                print("2- Gestionar opciones de administrador")
                print("3- Regresar")
                opcion = input("Eliga su opcion: ")

                if opcion == '1':
                    nuevaContrasena = input("Ingrese su nueva contrasena: ")
                    cambiarContrasena(usuarioActual.curp, nuevaContrasena)
                    administrativos = recopilarAdministrativos()

                elif (usuario == 'CURP1') and (opcion == '2'):
                    '''
                    En esta parte únicamente puede ingresar el administrador
                    principal, de esta forma cuenta con acciones extras 
                    desplegadas en otro menú
                    '''
                    system("cls")
                    print("1- Registrar administrativo")
                    print("2- Dar de baja a un administrativo")
                    print("3- Dar informacion de algun administrativo")
                    print("4- Ver administrativos")
                    print("5- Regresar")
                    opcion = input("Eliga su opcion: ")

                    if opcion == '1':
                        system("cls")
                        curp = input("Ingrese el curp: ")
                        nombre = input("Ingrese el nombre: ")
                        correo = input("Ingrese el correo: ")
                        numeroDeTelefono = input("Ingrese el numero de telefono: ")
                        contrasena = input("Ingrese la contraseña: ")
                        registrarNuevoAdministrativo(curp, nombre, correo, numeroDeTelefono, contrasena)
                        administrativos = recopilarAdministrativos()
                    
                    elif opcion == '2':
                        system("cls")
                        curp = input("Ingrese el curp del administrativo a dar de baja: ")
                        if curp != usuarioActual.curp:
                            darDeBajaAdministrativo(curp, medicos)
                            administrativos = recopilarAdministrativos()
                        else:
                            print("El administrador no se puede dar de baja a sí mismo")

                    elif opcion == '3':
                        system("cls")
                        existe = False
                        curp = input("Ingrese el curp del administrativo que quiera revisar: ")
                        for i in administrativos:
                            if i["curp"] == curp:
                                print(i, "\n")
                                existe = True
                        if not existe:        
                            print("Ese curp no existe, intenta de nuevo")
                    
                    elif opcion == '4':
                        system("cls")
                        for i in administrativos:
                            print(i, "\n")

                    elif opcion == '5':
                        break

                elif opcion == '3':
                    break

                else: 
                    system("cls")
                    print("No tiene permisos para esto\n")

        elif opcionMenu == '3':
            system("cls")
            while True:
                '''
                En esta parte se encuentra la gestión de los productos
                disponibles, cualquier usuario puede agregar, vender, 
                abastecer, comprobar y ver el almacén
                '''
                print("1- Agregar producto")
                print("2- Vender producto")
                print("3- Abastecer producto")
                print("4- Comprobar existencia de producto")
                print("5- Ver almacen")
                print("6- Salir")

                opcion = input("Eliga su opcion: ")

                if opcion == '1':
                    system("cls")
                    nombre = input("Ingrese el nombre: ")
                    marca = input("Ingrese la marca: ")
                    precio = validarEntero(input("Ingrese el precio: "))
                    cantidad = validarEntero(input("Ingrese la cantidad: "))
                    agregarProductos(nombre, marca, precio, cantidad)
                    almacen = recopilarDatos()

                elif opcion == '2':
                    system("cls")
                    codigo = input("Ingrese el codigo de barras: ")
                    try:
                        cantidad = int(input("Ingrese cantidad: "))
                    except:
                        print("ERROR! Ingrese valores válidos")
                        continue
                    if cantidad <= 0:
                        print("ERROR! Ingrese valores válidos")
                        continue
                    venderProducto(codigo, almacen, cantidad)
                    almacen = recopilarDatos()

                elif opcion == '3':
                    system("cls")
                    codigo = input("Ingrese el codigo de barras: ")
                    try:
                        cantidad = int(input("Ingrese cantidad: "))
                    except:
                        print("ERROR! Ingrese valores válidos")
                        continue
                    if cantidad <= 0:
                        print("ERROR! Ingrese valores válidos")
                        continue
                    comprarProducto(codigo, almacen, cantidad)
                    almacen = recopilarDatos()

                elif opcion == '4':
                    system("cls")
                    existe = False
                    codigo = input("Ingrese el código de barras que quiera comprobar: ")
                    for i in almacen:
                        if i["codigoDeBarras"] == codigo:
                            print(f'Hay {i["_cantidadEnAlmacen"]} {i.darNombre()} de la marca {i.darMarca()} en el almacen')
                            existe = True
                    if not existe:        
                        print("Ese codigo de barras no existe, intenta de nuevo")

                elif opcion == '5':
                    system("cls")
                    for i in almacen: 
                        print(i.descripcion())

                elif opcion == '6':
                    system("cls")
                    break

        elif opcionMenu == '4':
            system("cls")
            break

    if not correcto:
        system("cls")
        print("Datos erroneos, intente de nuevo\n")

    opcion = input("Ingrese 1 para salir o ingrese cualquier otra tecla para iniciar sesion: ")
    if opcion == '1':
        break
    system("cls")




