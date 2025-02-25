import clase47ConexionOracle


#claseDatos=clase47ConexionOracle()

###
#clase47ConexionOracle.conexionOracleEnfermos()

#print("Probando clase de Oracle: ENFERMOS")
#print("Introduzca una inscripcion a eliminar")
#inscripcion=int(input())
#conexion=clase47ConexionOracle.conexionOracleEnfermos()
#eliminados=conexion.EliminaEnfermos(inscripcion)
#print(f"Enfermos Eliminados : {eliminados}")
###

clase47ConexionOracle.conexionOracleEnfermos()

print("introduzca nuevo apellido")
nuevo_apellido=str(input())
print("Introduzca una inscripcion a modificar")
inscripcion=int(input())
conexion=clase47ConexionOracle.conexionOracleEnfermos()

modificados=conexion.modificarApellidoEnfermoPorInscripcion(inscripcion, nuevo_apellido)
print(f"Enfermos modificados : {modificados}")