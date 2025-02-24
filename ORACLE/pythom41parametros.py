import oracledb
print("parametros ORACLE")
conexion= oracledb.connect(user='SYSTEM',password='oracle', dsn='localhost/xe')


print("Introduzca el numero de departamento ")
iddept= input()
sql=f"select * from EMP where DEPT_NO={iddept}"

#print(sql)

cursor = conexion.cursor()
cursor.execute(sql)


for fila in cursor:
    print(f"Apellido: {fila[1]}, Oficio: {fila[2]} , Departamento {fila[7]}")


cursor.close()
conexion.close()