import psycopg2
import psycopg2.extras
from Personal import PersonalMedico
from Producto import *

hostname = "localhost"
database = "ProyectoFinal"
username = "postgres"
pwd = "Hecyor1234"
port_id = 5432
lista = []

def crearCodigoDeBarras(nombre, marca, precio):
    precio = str(precio)
    if len(precio) == 1:
        precio = '0' + precio
    return nombre[0:2].upper() + marca[0:2].upper() + precio[0:2]

def inicializarTabla():
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

def comprarProducto(codigo_de_barras, lista, cantidad):
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

def inicializarTablaPersonalMedico():
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



                
            





    



