print(f"introduce el  numero a mostrar")
numero1 = int(input())

while (numero1 != 1):
    if (numero1 % 2 == 0 ):
        numero1 = int(numero1 / 2)
    else:
        numero1=numero1 * 3 + 1
    print(numero1)