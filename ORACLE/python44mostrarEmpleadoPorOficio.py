import oracledb

        
conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
if conexion:
    print(f".....conexion correcta { conexion}")



    

sqlOficios="""
                SELECT DISTINCT oficio
                FROM emp
                """
cursorOficios=conexion.cursor()
cursorOficios.execute(sqlOficios)
contador = 1
listaOficios=[]
for fila in cursorOficios:
        print(f"{contador} - {fila[0]}")
        listaOficios.append(fila[0])
        #print(f"{contador} - {fila[0]}")
        contador=contador + 1

cursorOficios.close()
#rint(oficios)
print(f"introduzca un oficio")
opcion = int(input())
oficio=listaOficios[opcion - 1]


sqlEmpleado="""
                SELECT  *
                FROM emp
                where oficio = :oficio
                """
cursor=conexion.cursor()
cursor.execute(sqlEmpleado, (oficio, ))
for fila in cursor:
        #oficios=oficios.append(fila)
        print(fila)
#rint(oficios)

cursor.close()
 
conexion.close()

