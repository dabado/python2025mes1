import oracledb



conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
print(f".....conexion correcta { conexion}")
sql ="select * from DEPT"
cursor = conexion.cursor()
cursor.execute(sql)
fila=cursor.fetchone()

print(f"muestar una fila1 :  {fila}")
fila=cursor.fetchone()
print(f"muestar una fila2 :  {fila}")
fila=cursor.fetchone()
print(f"muestar una fila3 :  {fila}")
fila=cursor.fetchone()
print(f"muestar una fila4 :  {fila}")
fila=cursor.fetchone()
print(f"muestar una fila5 :  {fila}")



#for i in len(fila):
 #   fila=cursor.fetchone()
  #  print(fila)
   




cursor.close()
conexion.close()
