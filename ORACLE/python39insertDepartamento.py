import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")


print("indicanos el id depeartamento a dar de alta")
iddata=str(input())
print("indicanos el la localidad a dar de alta")
localidaddata=str(input())
print("indicanos el nombre de departamento a dar de alta")
departNamedata=str(input())

sql=("insert into DEPT values(" + iddata + ",'" + departNamedata + "','" + localidaddata + "')") 
print(str(sql))
#print(sql)

cursor=conexion.cursor()
cursor.execute(sql)
afectados = str(cursor.rowcount)
conexion.commit()
#elimina el enfermo sin el commit , como es distinta sesion desde sql dev se vé aun
print(f"afectados: {afectados}")
print(f"cerramos cursor {cursor.close()}")

#ahora el cursor esta cerrado y podemos hacer consultas sobre el mismo cursor
sqlselect="select * from DEPT"
cursor=conexion.cursor()
cursor.execute(sqlselect)
for file in cursor:
    print(str(file[0]), str(file[1]))
cursor.close()

conexion.close()
print(f"fin de la ejecucion")
