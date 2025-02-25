import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")


print("indicanos el codigo de hospital a incrementar")
hospitalCod=int(input())
print(f"indicanos  la cantidad a incrementar al salario para hospital codigo : {hospitalCod}")
incremento=int(input())
sql="select * from PLANTILLA where HOSPITAL_COD=:hospitalCod"
#print(f"sentencia: {sql}")
cursor = conexion.cursor()
cursor.execute(sql, (hospitalCod, ))
for fila in cursor:
    print(fila)
print("encontrados :" + str(cursor.rowcount))


cursor.close()

sqlupdate = "update PLANTILLA set SALARIO = salario + :sala where HOSPITAL_COD = :hospitalCod" 
cursor = conexion.cursor()
cursor.execute(sqlupdate, (incremento, hospitalCod))


print("modificados :" + str(cursor.rowcount))
import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")


print("indicanos el codigo de hospital a incrementar")
hospitalCod=int(input())
print(f"indicanos  la cantidad a incrementar al salario para hospital codigo : {hospitalCod}")
incremento=int(input())


sql="select * from PLANTILLA where HOSPITAL_COD=:hospitalCod"
#print(f"sentencia: {sql}")
cursor = conexion.cursor()
cursor.execute(sql, (hospitalCod, ))
for fila in cursor:
    print(fila)
print("encontrados :" + str(cursor.rowcount))
cursor.close()


sqlupdate = "update PLANTILLA set SALARIO = salario + :sala where HOSPITAL_COD = :hospitalCod" 
cursor = conexion.cursor()
cursor.execute(sqlupdate, (incremento, hospitalCod))
print("modificados :" + str(cursor.rowcount))
print(cursorupdate.bindnames())



cursor.execute(sql, (hospitalCod, ))
for fila in cursor:
    print(fila)
conexion.commit()
cursor.close()
cursorupdate.close()
conexion.close()
