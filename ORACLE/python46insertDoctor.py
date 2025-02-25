import oracledb

        
conexion=(oracledb.connect( user="system", password="oracle",dsn="localhost/xe"))
if conexion:
    print(f".....conexion correcta { conexion}")


sqlHOSPITAL = "select distinct Hospital_cod FROM doctor"
cursor=conexion.cursor()
cursor.execute(sqlHOSPITAL)
contador = 1
listaHospitales=[]
for fila in cursor:
    print(f"{contador} - {fila[0]}")
    listaHospitales.append(fila[0])
    
    contador = contador + 1

cursor.close()


print("introduzca un Apellido del doctor")
Apellido=str(input())
print("introduzca un Especialidad del doctor")
Especialidad=str(input())
print("introduzca Salario del doctor")
Salario=str(input())

print("Seleccione un Hospital para el doctor")
seleccion=int(input())
Hospital=listaHospitales[seleccion - 1]
#turno = "T"
sqlDoctores="select max(DOCTOR_NO) as MAXIMO from DOCTOR"
cursorEmpleados=conexion.cursor()
cursorEmpleados.execute(sqlDoctores)
file = cursor.fetchone()
idDoctor=file[0]



cursorEmpleados.close()
sqlInsert="""
          insert into doctor values (:Hospital, :idDoctor, :apellido, :salario)  
"""
cursorInsert=conexion.cursor()
cursorInsert.execute(sqlInsert, (Hospital, idDoctor, Apellido, Salario))
conexion.close()