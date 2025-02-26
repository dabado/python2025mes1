import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")


print("indicanos el oficio a incrementar")
oficioX=str(input())
print(f"indicanos  la cantidad a incrementar al salario para {oficioX}")
incremento=int(input())
sql="select * from EMP where OFICIO=:oficioX"
print(f"sentencia: {sql}")
cursor = conexion.cursor()
cursor.execute(sql, (oficioX, ))
for fila in cursor:
    print(fila)
print("encontrados :" + str(cursor.rowcount))

cursor.close()
#mivalor = 10
#sql1 = "select * from EMP where DEPT_NO=:mivalor"
#cursor.execute(sql1, (mivalor,))


cursor = conexion.cursor()
sqlupdate="update  EMP set SALARIO = SALARIO + :incrementar where OFICIO = :oficiofiltro"
#print(f"sentencia sql : {sqlupdate}")


cursor.execute(sqlupdate, (incremento, oficioX, ))
print("filas modificadas :" + str(cursor.rowcount))


conexion.commit()
cursor.close()

sql="select APELLIDO; OFICIO; SALARIO from EMP where OFICIO=:oficioX"
print(f"sentencia: {sql}")
cursor = conexion.cursor()
cursor.execute(sql, (oficioX, ))
for ape, ofi, sala in cursor:
    print(f"{ape},{ofi},{sala}")
    
cursor.close()
conexion.close()
print(f"fin de la ejecucion")
