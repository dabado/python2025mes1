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
#print(sql)

cursor=conexion.cursor()
cursor.execute(sql)
afectados = str(cursor.rowcount)
conexion.commit()