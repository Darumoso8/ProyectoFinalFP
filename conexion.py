import psycopg2
import psycopg2.extras
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

def recopilarDatos():
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
                            precio                  int NOT NULL,
                            cantidad_En_Almacen     int NOT NULL) """

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
            cur.execute("SELECT * FROM PRODUCTOS")
                    
            for i in cur.fetchall():
                ejemplo = Producto(
                            i["codigo_de_barras"],
                            i["nombre"],
                            i["marca"], 
                            i["precio"],
                            i["cantidad_en_almacen"])
                lista.append(ejemplo)
    conn.close()
    return lista

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

            crear_tabla = """ CREATE TABLE IF NOT EXISTS productos (
                            codigo_De_Barras        text PRIMARY KEY NOT NULL, 
                            nombre                  text NOT NULL,
                            marca                   text NOT NULL,
                            precio                  int NOT NULL,
                            cantidad_En_Almacen     int NOT NULL) """
            cur.execute(crear_tabla)

            if codigo_de_barras not in codigosDeBarras:
                insertar_informacion = "INSERT INTO productos (codigo_De_Barras, \
                                nombre, marca, precio, \
                                cantidad_En_Almacen) \
                                VALUES (%s, %s, %s, %s, %s)"
            
                insertar_valores = (
                            codigo_de_barras,  nombre,
                            marca, precio, cantidad)
            
                cur.execute(insertar_informacion, insertar_valores)
            
            else:
                print("Ese codigo de barras ya existe")

def venderProducto(codigo_de_barras):
    eliminarProducto = 'DELETE FROM productos WHERE codigo_de_barras = %s'
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
            if codigo_de_barras in codigosDeBarras:
                ganancia = codigo_de_barras
                cur.execute(eliminarProducto, (codigo_de_barras,))
            else:
                print("Ese codigo de barras no existe")
                
            
                
            





    



