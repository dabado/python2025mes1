from libreria24matematicas import sumar, restar, multiplicar, mostrarMenu

print("calculadora con metodos")

numero1=9
numero2=4

print(sumar(10, 40))

mostrarMenu()
opcion=int(input())
resultado=0
if (opcion == 1):
    resultado = sumar(numero1, numero2)
elif (opcion == 2) :
    resultado = restar(numero1, numero2)
elif (opcion == 3):
    resultado = multiplicar(numero1, numero2)
else:
    print("opcion incorrecta")
print(f"resultado: ", resultado)
print(f"fin de programa")