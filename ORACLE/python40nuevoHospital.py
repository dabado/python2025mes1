import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")


print("indicanos el id del hospital a dar de alta")
iddata=str(input())
print("indicanos  la direccion a dar de alta")
direcciondata=str(input())
print("indicanos  el nombre a dar de alta")
nombreddata=str(input())
print("indicanos  el telefono a dar de alta")
telefonodata=str(input())
print("indicanos numero de camas a dar de alta")
camasdatadata=str(input())

sql=("insert into HOSPITAL values(" + iddata + ",'" + nombreddata + "','" + direcciondata + "','" + telefonodata + "','" + camasdatadata + "')") 
print(str(sql))

#sql=f"insert into HOSPITAL values({iddata} , {nombreddata} , {direcciondata} , {telefonodata} ,  {camasdatadata }"
cursor=conexion.cursor()
cursor.execute(sql)
print("filas insertadas :" + str(cursor.rowcount))
#afectados = str(cursor.rowcount)
conexion.commit()
cursor.close()
sqlread="select * from HOSPITAL"
cursor=conexion.cursor()
cursor.execute(sqlread)
for fila in cursor:
    print(fila)
cursor.close()
conexion.close()