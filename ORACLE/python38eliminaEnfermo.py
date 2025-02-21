import oracledb




print("indicanos el numero de incripcion de enfermo a dar de baja ")
data=str(input())
sql=("delete from ENFERMO where INSCRIPCION='" + data + "'")
print(sql)
conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")
cursor=conexion.cursor()
cursor.execute(sql)
afectados = str(cursor.rowcount)
conexion.commit()
#elimina el enfermo sin el commit , como es distinta sesion desde sql dev se vé aun
print(f"afectados: {afectados}")
print(f"cerramos cursor {cursor.close()}")
print(f"cerramos conexion {conexion.close()}")

