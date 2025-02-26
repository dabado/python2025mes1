import oracledb


conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))

print(f".....conexion correcta { conexion}")

sql="select APELLIDO, OFICIO  ,(SALARIO + COMISION) as SUELDO  from emp UNION select APELLIDO,ESPECIALIDAD ,SALARIO  from DOCTOR "
cursor=conexion.cursor()
cursor.execute(sql)
if(not cursor):
    print("sin contenido en cursor")
else:
    print("si existen datos en cursor")
fila = cursor.fetchone()
if(not fila):
    print("sin contenido en fila")
else:
    print("si existen datos")
nombre=fila[0]
empleo=fila[1]
print(f"empleo: {empleo}")
print(f"fila: {fila}")

cursor.execute(sql)

for i in cursor:
    print(f"datosfor: {i}")




print(f"cerramos cursor {cursor.close()}")
print(f"cerramos conexion {conexion.close()}")

