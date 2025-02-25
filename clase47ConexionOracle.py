import oracledb


class conexionOracleEnfermos():

    def __init__(self):
        
        self.conexion = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')
        conexion=self.conexion
        if conexion:
            print(f".....conexion correcta { conexion}")
       
    def EliminaEnfermos(self, inscripcion):
        cursor = self.conexion.cursor()
        sql="delete from ENFERMO where INSCRIPCION=:inscripcion"
        #print(sql)
        cursor.execute(sql, (inscripcion, ))
        afectados = str(cursor.rowcount)
        self.conexion.commit()
        cursor.close()
        #elimina el enfermo sin el commit , como es distinta sesion desde sql dev se vé aun
        print(f"afectados: {afectados}")
        
        print(f"cerramos conexion {self.conexion.close()}")
        return afectados

    def modificarApellidoEnfermoPorInscripcion(self, inscripcion, nuevo_apellido):
        
        
        sql="""
                update  ENFERMO 
                set  APELLIDO=:nuevo_apellido
                where INSCRIPCION=:inscripcion
                """
        print(sql)
        cursor = self.conexion.cursor()
        cursor.execute(sql, (inscripcion, nuevo_apellido ))
        afectados = str(cursor.rowcount)
        #cursor.close()
        return afectados


    def incrementarSalarioPorOficio(self):
        print("indicanos el oficio a incrementar")
        oficioX=str(input())
        print(f"indicanos  la cantidad a incrementar al salario para {oficioX}")
        incremento=int(input())
        sql="select * from EMP where OFICIO=:oficioX"
        print(f"sentencia: {sql}")
        cursor = self.conexion.cursor()
        cursor.execute(sql, (oficioX, ))
        for fila in cursor:
            print(fila)
        print("encontrados :" + str(cursor.rowcount))

        cursor.close()


        cursor = self.conexion.cursor()
        sqlupdate="update  EMP set SALARIO = SALARIO + :incrementar where OFICIO = :oficiofiltro"
        #print(f"sentencia sql : {sqlupdate}")


        cursor.execute(sqlupdate, (incremento, oficioX, ))
        print("filas modificadas :" + str(cursor.rowcount))


        self.conexion.commit()
        cursor.close()

        sql="select APELLIDO; OFICIO; SALARIO from EMP where OFICIO=:oficioX"
        print(f"sentencia: {sql}")
        cursor = self.conexion.cursor()
        cursor.execute(sql, (oficioX, ))
        for ape, ofi, sala in cursor:
            print(f"{ape},{ofi},{sala}")
            
        cursor.close()
        self.conexion.close()
        print(f"fin de la ejecucion")


