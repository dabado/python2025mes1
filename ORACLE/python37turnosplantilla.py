import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))

print(f".....conexion correcta { conexion}")
print("indicanos el turno ")
data=str(input())
sql=(f"select APELLIDO,FUNCION from plantilla where TURNO='{data}'")
print(sql)
cursor=conexion.cursor()
cursor.execute(sql)


for apell,puesto in cursor :
    print(f"los apellidos son {apell} y trabaja de funcion de {puesto}")


print(f"cerramos cursor {cursor.close()}")
print(f"cerramos conexion {conexion.close()}")