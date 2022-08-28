import psycopg2
import psycopg2.extras

hostname = "localhost"
database = "ProyectoFinal"
username = "postgres"
pwd = "Hecyor1234"
port_id = 5432

with psycopg2.connect(host = hostname, 
                        dbname = database, 
                        user = username, 
                        password = pwd, 
                        port = port_id) as conn:

    with conn.cursor(cursor_factory = psycopg2.extras.DictCursor) as cur:

        cur.execute("DROP TABLE IF EXISTS productos")
        crear_tabla = """ CREATE TABLE IF NOT EXISTS Productos (
                        codigo_De_Barras        varchar(6) PRIMARY KEY NOT NULL, 
                        nombre                  varchar(40) NOT NULL,
                        marca                   varchar(40) NOT NULL,
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

        for i in insertar_valores:
            cur.execute(insertar_informacion, i)

        cur.execute("SELECT * FROM PRODUCTOS")

        for i in cur.fetchall():
            print(i["nombre"], i["marca"], i["precio"], i["cantidad_en_almacen"])

conn.close()