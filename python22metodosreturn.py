
def convertirMayusculas(data):
    resultado = data.upper()
    return resultado

def convertirMinusculas(data):
    resultado=data.lower()
    return resultado 

def concatenar(data1, data2):
    resultado= data1 + data2
    return resultado




def mostrarMenu():
    print("selecciona una opcion:")
    print("1_ convertir en mayusculas")
    print("2_ convertir en minusculas")
    print("3_ concatenar textos")
    print("4_ salir")
    
print("Metodos return")
print("Introduzca un texto")
valor=input()
mostrarMenu()
opcion=int(input())

#while opcion != 4:
if opcion == 1:
        resultado=convertirMayusculas(valor)
elif opcion == 2:
        resultado=convertirMinusculas(valor)
elif opcion == 3:
        print("ponga otro texto")
        otro = input()
        resultado=concatenar(valor, otro)
elif opcion == 4:
        exit
    
print(resultado)
print("final de programa")
    
