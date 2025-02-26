import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))

print(f".....conexion correcta { conexion}")

inscribe=(f"dame el numero de inscripcion")
print(inscribe)
data=str(input())
sql=(f"select APELLIDO, DIRECCION  from ENFERMO where INSCRIPCION={data}") 


cursor=conexion.cursor()
cursor.execute(sql)
for i in cursor :
    print(i)


print(f"cerramos cursor {cursor.close()}")
print(f"cerramos conexion {conexion.close()}")