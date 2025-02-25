import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")


print("indicanos el codigo de hospital a incrementar")
hospitalCod=int(input())
print(f"indicanos  la cantidad a incrementar al salario para hospital codigo : {hospitalCod}")
incremento=int(input())
sql="""
    select * from PLANTILLA
    where HOSPITAL_COD=:hospitalCod
    """
#print(f"sentencia: {sql}")
cursor = conexion.cursor()
cursor.execute(sql, (hospitalCod, ))
for fila in cursor:
    print(fila)
print("encontrados :" + str(cursor.rowcount))
print(cursor.bindnames())

# no cierro el cursor para hacer recuperar resultado cursor.close()

sqlupdate = """
            update PLANTILLA 
            set SALARIO = salario + :incremento 
            where HOSPITAL_COD = :hospitalCod
            """
cursorupdate = conexion.cursor()


cursorupdate.execute(sqlupdate, (incremento, hospitalCod))

print("modificados : incrementados "+ str(incremento) + " en " + str(cursorupdate.rowcount) + " modificados." )


print(cursorupdate.bindnames())
cursor.execute(sql, (hospitalCod, ))
for fila in cursor:
    print(fila)
conexion.commit()
cursor.close()
cursorupdate.close()
conexion.close()
