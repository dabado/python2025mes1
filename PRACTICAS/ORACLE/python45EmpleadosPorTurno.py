import oracledb

        
conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
if conexion:
    print(f".....conexion correcta { conexion}")


sqlTurnos = """
            select distinct TURNO, case TURNO 
            when 'M' then 'Mañana' 
            when 'T' then 'Tarde' 
            else 'Noche' end as VALOR 
            FROM plantilla
            """
cursor=conexion.cursor()
cursor.execute(sqlTurnos)
contador = 1
listaTurnos=[]
for fila in cursor:
    listaTurnos.append(fila[0])
    print(f"{contador} - {fila[1]}")
    contador = contador + 1

cursor.close()


print("Seleccione un turno")
seleccion=int(input()) - 1
turno=listaTurnos[seleccion]
#turno = "T"
sqlempleados="""select *
                from plantilla 
                where TURNO = :P1 
                """
cursorEmpleados=conexion.cursor()
cursorEmpleados.execute(sqlempleados, (turno, ))
#print(cursorEmpleados.rowcount)
for fila in cursorEmpleados:
    print(fila)


cursorEmpleados.close()


conexion.close()