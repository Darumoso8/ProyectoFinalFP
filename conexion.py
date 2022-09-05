import psycopg2
import psycopg2.extras
from Personal import PersonalAdministrativo, PersonalMedico
from Producto import *

"""
Aqui se almacenan los valores necesarios para establecer una conexión
con la base de datos
"""
hostname = "localhost"
database = "ProyectoFinal"
username = "postgres"
pwd = "Hecyor1234"
port_id = 5432
lista = []

# Las siguientes funciones se encargan del funcionamiento de los productos
def crearCodigoDeBarras(nombre, marca, precio):
    '''
    La función crea el código de barras siguiendo la siguiente regla: 
    NNMMPP, donde NN son las dos primeras letras del nombre, MM las
    dos primeras letras de la marca y PP los dos primeros dígitos
    del precio (En caso de ser unidigital se pone un 0 antes)
    '''
    precio = str(precio)
    if len(precio) == 1:
        precio = '0' + precio
    return nombre[0:2].upper() + marca[0:2].upper() + precio[0:2]

def inicializarTabla():
    '''
    Esta funcion se conecta a la base de datos y crea una tabla 
    llamada productos (En caso de existir la borra y la crea de nuevo),
    además la llena con elementos que simulan serparte de un almacén
    ya existente
    '''
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:

        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            cur.execute("DROP TABLE IF EXISTS productos")
            crear_tabla = """ CREATE TABLE IF NOT EXISTS productos (
                            codigo_De_Barras        text PRIMARY KEY NOT NULL, 
                            nombre                  text NOT NULL,
                            marca                   text NOT NULL,
                            precio                  int NOT NULL CHECK (precio > 0),
                            cantidad_En_Almacen     int NOT NULL CHECK (cantidad_En_Almacen > 0)) """

            cur.execute(crear_tabla)


            insertar_informacion = "INSERT INTO productos (codigo_De_Barras, \
                                    nombre, marca, precio, \
                                    cantidad_En_Almacen) \
                                    VALUES (%s, %s, %s, %s, %s)"

            insertar_valores = [("TAHO23",  "Tapete",       "House",        234,    7),
                                ("CHPU75",	"Champu",	    "Purina",	    75,	    12),
                                ("CHPE62",	"Champu",	    "Pedegree",	    62,	    15),
                                ("CHES96",	"Champu",	    "Espree",	    96,	    4),
                                ("JAPE38",	"Jabón",	    "Pedegree",	    38,	    22),
                                ("JAES63",	"Jabón",	    "Espree",	    63,	    8),
                                ("JAPU52",	"Jabón",	    "Purina",	    52,	    16),
                                ("PEPE90",	"Peine",	    "Pedegree",	    90,	    3),
                                ("PLST17",	"Platos",	    "Steelware",	174,	6),
                                ("CRPE80",	"Croquetas",	"Pedegree",	    80,	    120),
                                ("CRNU14",	"Croquetas",	"Nupec",	    145,	160),
                                ("CRPU10",	"Croquetas",	"Purina",	    100,	80),
                                ("MEME63",	"Medicina",	    "Medilab",	    638,	2)]

            cur.executemany(insertar_informacion, insertar_valores)                    
    conn.close()

def recopilarDatos():
    ''' 
    Esta función toma los valores de la tabla y los instancia como 
    objetos de la clase Producto, además los guarda en una lista y
    regresa esa misma lista
    '''
    listaNueva = []
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            cur.execute("SELECT * FROM PRODUCTOS")      
            for i in cur.fetchall():
                ejemplo = Producto(
                            i["codigo_de_barras"],
                            i["nombre"],
                            i["marca"], 
                            i["precio"],
                            i["cantidad_en_almacen"])
                listaNueva.append(ejemplo)
    conn.close()
    return listaNueva

def agregarProductos(nombre, marca, precio, cantidad):
    '''
    Esta funcion agrega un producto nuevo a la base de datos, con
    ayuda de la función crearCodigoDeBarras le crea su codigo de barras
    , luego crea una lista con todos los codigos de barra para 
    comprobar que no sea un codigo repetido, de no estar repetido, 
    inserta el nuevo producto
    '''
    codigo_de_barras = crearCodigoDeBarras(nombre, marca, precio)
    codigosDeBarras = []
    lista = recopilarDatos()
    for i in range(len(lista)):
        codigosDeBarras.append(lista[i].codigoDeBarras)

    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            if codigo_de_barras not in codigosDeBarras:
                insertar_informacion = "INSERT INTO productos (codigo_De_Barras, \
                                    nombre, marca, precio, \
                                    cantidad_En_Almacen) \
                                    VALUES (%s, %s, %s, %s, %s)"
                  
                insertar_valores = (
                                codigo_de_barras, nombre, 
                                marca, precio, cantidad)
                try:
                    cur.execute(insertar_informacion, insertar_valores)
                except:
                    print("ERROR! Ingrese números válidos")
            else:
                print("Ya existe un producto con este número de barras")
    conn.close()
            
def venderProducto(codigo_de_barras, lista, cantidad):
    '''
    Esta función actualiza la cantidad en almacén de un producto dado, 
    tambien hace la comprobación que el código de barras exista, en
    caso de existir le resta la cantidad solicitada al producto, 
    sin embargo la cantidad de producto restante no puede ser negativa, 
    en caso de serlo se produce una excepción
    '''
    actualizarProducto = 'UPDATE productos SET cantidad_en_almacen = cantidad_en_almacen - %s WHERE codigo_de_barras = %s'
    codigosDeBarras = []

    for i in range(len(lista)):
        codigosDeBarras.append(lista[i].codigoDeBarras)
        
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            if codigo_de_barras in codigosDeBarras:
                try:
                    cur.execute(actualizarProducto, (cantidad, codigo_de_barras,))
                except:
                    print('ERROR! Ingrese números válidos')
            else:
                print("Ese codigo de barras no existe")
    conn.close()

def comprarProducto(codigo_de_barras, lista, cantidad):
    '''
    Esta funcion simula abastercer la cantidad en almacen de un 
    producto, crea una lista con todos los codigos de barra y en 
    caso de existir el solicitado le suma la cantidad requerida al
    almacen
    '''
    actualizarProducto = 'UPDATE productos SET cantidad_en_almacen = cantidad_en_almacen + %s WHERE codigo_de_barras = %s'
    codigosDeBarras = []

    for i in range(len(lista)):
        codigosDeBarras.append(lista[i].codigoDeBarras)
        
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            if codigo_de_barras in codigosDeBarras:
                try:
                    cur.execute(actualizarProducto, (cantidad, codigo_de_barras,))
                except:
                    print('ERROR! Ingrese números válidos')
            else:
                print("Ese codigo de barras no existe")
    conn.close()


# Las siguientes funciones se encargan de la gestión del personal médico
def inicializarTablaPersonalMedico():
    '''
    Esta función crea una tabla llamada personal (En caso de existir
    la borra y la crea de nuevo) además inserta valores predeterminados
    simulando médicos que ya trabajan ahí
    '''
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:

        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            cur.execute("DROP TABLE IF EXISTS personal")
            crear_tabla = """ CREATE TABLE IF NOT EXISTS personal (
                            curp                    text PRIMARY KEY NOT NULL, 
                            nombre                  text NOT NULL,
                            correo                  text NOT NULL,
                            numero_de_telefono      text NOT NULL,
                            especialidad            text NOT NULL )"""

            cur.execute(crear_tabla)

            insertar_informacion = "INSERT INTO personal (curp, \
                                    nombre, correo, numero_de_telefono, \
                                    especialidad) \
                                    VALUES (%s, %s, %s, %s, %s)"

            insertar_valores = [("CURP1",   "Javier Roman",        "correo@1.com",     "5621274871",    "Neurologo"),
                                ("CURP2",   "Luisa Martinez",	   "correo@2.com",	   "5618095628",	"Cardiologo"),
                                ("CURP3",	"Monica Maldonado",	   "correo@3.com",	   "5522914033",	"Nutriologo"),
                                ("CURP4",	"Hector Quiroz",	   "correo@4.com",	   "5588032873",	"Practicante")]
            cur.executemany(insertar_informacion, insertar_valores)                    
    conn.close()

def recopilarMedicos():
    ''' 
    Esta función toma los valores de la tabla y los instancia como 
    objetos de la clase PersonalMédico, además los guarda en 
    una lista y regresa esa misma lista
    '''    
    listaNueva = []
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM PERSONAL")      
            for i in cur.fetchall():
                ejemplo = PersonalMedico(
                            i["nombre"],
                            i["correo"],
                            i["numero_de_telefono"], 
                            i["curp"],
                            i["especialidad"])
                listaNueva.append(ejemplo)
    conn.close()
    return listaNueva

def registrarNuevoMedico(curp, nombre, correo, numero_de_telefono, especialidad):
    '''
    Crea una lista llamada curps donde se almacenan todas las curps,
    esta se compara con el curp ingresado como argumento para verificar
    que sea un curp válido, en caso de serlo se agrega el nuevo médico 
    a la BD.
    '''
    curps = []
    lista = recopilarMedicos()
    for i in range(len(lista)):
        curps.append(lista[i].curp)

    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            if curp not in curps:
                insertar_informacion = "INSERT INTO personal (curp, \
                                    nombre, correo, numero_de_telefono, \
                                    especialidad) \
                                    VALUES (%s, %s, %s, %s, %s)"
                  
                insertar_valores = (
                                curp, nombre, 
                                correo, numero_de_telefono, especialidad)
                try:
                    cur.execute(insertar_informacion, insertar_valores)
                except:
                    print("ERROR! Ingrese valores válidos")
            else:
                print("Ya existe un medico con este curp")
    conn.close()

def darDeBajaMedico(curp, lista):
    '''
    Esta función eleminia al médico cuyo curp coincida, 
    crea una lista vacía llamada curps la cual almacena todas
    las curps actuales, en caso de existir la curp, elimina a ese 
    méidco de la BD. 
    '''
    borrarMedico = 'DELETE FROM personal WHERE curp = %s'
    curps = []

    for i in range(len(lista)):
        curps.append(lista[i].curp)
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            if curp in curps:
                try:
                    cur.execute(borrarMedico, (curp,))
                except:
                    print('ERROR! Ingrese valores válidos')
            else:
                print("Ese curp no existe")
    conn.close()

# Las siguientes funciones se encargan de la gestión del personal administratico

def inicializarTablaPersonalAdministrativo():
    '''
    Esta función crea una tabla llamada personalad (En caso de existir
    la borra y la crea de nuevo) además inserta valores predeterminados
    simulando administrativos que ya trabajan ahí.
    '''
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:

        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            cur.execute("DROP TABLE IF EXISTS personalad")
            crear_tabla = """ CREATE TABLE IF NOT EXISTS personalad (
                            curp                    text PRIMARY KEY NOT NULL, 
                            nombre                  text NOT NULL,
                            correo                  text NOT NULL,
                            numero_de_telefono      text NOT NULL,
                            contrasena              text NOT NULL )"""

            cur.execute(crear_tabla)

            insertar_informacion = "INSERT INTO personalad (curp, \
                                    nombre, correo, numero_de_telefono, \
                                    contrasena) \
                                    VALUES (%s, %s, %s, %s, %s)"

            insertar_valores = [("CURP1",   "Cristan Patiño",      "correoad@1.com",   "5539403432",    "12345"),
                                ("CURP2",   "Marta Mijares",	   "correoad@2.com",   "5513296528",	"12345"),
                                ("CURP3",   "Josue Ochoa",         "correoad@3.com",   "5578385839",    "12345")]
            cur.executemany(insertar_informacion, insertar_valores)                    
    conn.close()

def recopilarAdministrativos():
    '''
    La función recopilarAdministrativos toma los valores de la tabla 
    personalad y los instancia como objetos de la clase 
    PersonalAdministrativo, además los guarda en una lista y regresa
    esa misma lista
    '''
    listaNueva = []
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute("SELECT * FROM PERSONALAD")      
            for i in cur.fetchall():
                ejemplo = PersonalAdministrativo(
                            i["nombre"],
                            i["correo"],
                            i["numero_de_telefono"],
                            i["contrasena"], 
                            i["curp"])
                listaNueva.append(ejemplo)
    conn.close()
    return listaNueva

def registrarNuevoAdministrativo(curp, nombre, correo, numero_de_telefono, contrasena):
    '''
    Crea una lista llamada curps donde se almacenan todas las curps de
    los administrativos, esta se compara con el curp ingresado como 
    argumento para verificar que sea un curp válido, en caso de 
    serlo se agrega el nuevo administrativo a la BD.
    '''
    curps = []
    lista = recopilarAdministrativos()
    for i in range(len(lista)):
        curps.append(lista[i].curp)

    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

            if curp not in curps:
                insertar_informacion = "INSERT INTO personalad (curp, \
                                    nombre, correo, numero_de_telefono, \
                                    contrasena) \
                                    VALUES (%s, %s, %s, %s, %s)"
                  
                insertar_valores = (
                                curp, nombre, 
                                correo, numero_de_telefono, contrasena)
                try:
                    cur.execute(insertar_informacion, insertar_valores)
                except:
                    print("ERROR! Ingrese valores válidos")
            else:
                print("Ya existe un administrativo con este curp")
    conn.close()

def darDeBajaAdministrativo(curp, lista):
    '''
    Esta función elimina al administrativo cuyo curp coincida, 
    crea una lista vacía llamada curps la cual almacena todas
    las curps actuales, en caso de existir la curp, elimina a ese 
    administrativo de la BD. 
    '''
    borrarAdministrativo = 'DELETE FROM personalad WHERE curp = %s'
    curps = []

    for i in range(len(lista)):
        curps.append(lista[i].curp)
        
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            if curp in curps:
                try:
                    cur.execute(borrarAdministrativo, (curp,))
                except:
                    print('ERROR! Ingrese valores válidos')
            else:
                print("Ese curp no existe")
    conn.close()

def cambiarContrasena(curp, nuevaContrasena):
    '''
    Esta función cambia la contraseña del administrativo con el curp
    dado y la reemplaza con la contraseña nueva
    '''
    actualizarPersonalad = 'UPDATE personalad SET contrasena = %s WHERE curp = %s'
  
    with psycopg2.connect(host = hostname, 
                            dbname = database, 
                            user = username, 
                            password = pwd, 
                            port = port_id) as conn:
    
        with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:
            cur.execute(actualizarPersonalad, (nuevaContrasena, curp,))

    conn.close()

                
            





    



