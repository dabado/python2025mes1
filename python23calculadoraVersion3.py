
def sumar(num1, num2):
    resultado = int(num1) + int(num2) 
    return resultado

def restar(num1, num2):
    resultado = int(num1) - int(num2) 
    return resultado 

def multiplicar(num1, num2):
    resultado = int(num1) * int(num2) 
    return resultado

def mostrarMenu():
    print("selecciona una opcion:")
    print("0_ salir")
    print("1_ sumar")
    print("2_ restar")
    print("3_ multiplica")
    print("4_ introducir numeros de nuevo")


    
print("Metodos return")

print("Introduzca el primer numnero")
num1=input()
while num1.isdigit() == False:
    print("tiene que introducir un numero1")
    num1=input()
print(f"numero1 guardado {num1}")


      
print("introduzca el segundo numero")
num2=input()
while num2.isdigit() == False:
    print("tiene que introducir un numero2")
    num2=input()
print(f"numero2 guardado {num2}")




#mostrarMenu()
opcion=99

while (opcion != 0):
    mostrarMenu()
    opcion=int(input())

    if opcion == 1:
            resultado=sumar(num1, num2)
            print(resultado)
    elif opcion == 2:
            resultado=restar(num1, num2)
            print(resultado)
    elif opcion == 3:
            resultado = multiplicar(num1, num2)
            print(resultado)
    elif opcion == 4:
            print("Introduzca el primer numnero")
            num1=input()
            print("introduzca el segundo numero")
            num2=input()
    elif opcion == 0:
            resultado = "ha elegido salir .. saliendo" 
            print(resultado)
    else:
          print("opcion incorrecta, seleccione de nuevo")
            
    
#print(resultado)
print("final de programa")