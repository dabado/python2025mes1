print(f"introduce el primer numero")
numero1 = int(input())
print(f"introduce el segundo numero")
numero2 = int(input())
print(f"introduce el tercer numero")
numero3 = int(input())

mayor = 0
menor = 0
intermedio = 0

if (numero1 > numero2 and numero1 > numero3):
    print(f"el mayor es {numero1}")
    mayor = numero1
elif (numero2 > numero1 and numero2 > numero3):
    print(f"el mayor es {numero2}")
    mayor = numero2
elif (numero3 > numero1 and numero3 > numero2):
    print(f"el mayor es {numero3}")
    mayor = numero3
elif (numero1 > numero2 and numero1 < numero3):
    print(f"el intermedio es numero1")
    intermedio = numero1
elif (numero2 > numero1 and numero2 < numero3):
    print(f"el intermedio es numero2")
    intermedio = numero2
elif (numero3 >= numero1 and numero3 < numero2):
    print(f"el intermedio es numero3")
    intermedio = numero3
elif (numero1 < numero3 and numero1 < numero2):
    print(f"el menor es numero1")
    menor = numero1
elif (numero2 < numero1 and numero2 < numero3):
    print(f"el menor es numero2")
    menor = numero2
elif (numero3 < numero1 and numero3 < numero2):
    print(f"el menor es numero3")
    menor = numero3


suma = numero1 + numero2 + numero3
intermedio = suma - mayor - menor

print(f"el mayor es {mayor}, el intermedio es {intermedio}, y el menor es {menor}")
