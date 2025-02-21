import oracledb

conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))

print(f".....conexion correcta { conexion}")

sql ="select * from DEPT"
cursor=conexion.cursor()
cursor.execute(sql)


for i in cursor:
    print(f"TODAS: {i}")
    print(f"numero departamento: {i[0]}")
    print(f"departamento: {i[1]}")
    print(f"ciudad: {i[2]}")

cursor=conexion.cursor()
cursor.execute(sql)

###
for numdepartamento, departamento, ciudad in cursor:
    print(f"dep: {departamento}, ciudad : {ciudad} , numeroDEP: {numdepartamento}")

print(f"cerramos cursor {cursor.close()}")
print(f"cerramos conexion {conexion.close()}")
