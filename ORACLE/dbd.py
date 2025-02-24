
import oracledb


def abrir_con():
    conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
    cursor = conexion.cursor()
    print(f".....conexion establecida { conexion }")


def cerrar_con():
    cursorclose=cursor.close()
    conexionclose=connection.close()

abrir_con()
cerrar_con()