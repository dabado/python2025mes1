print(f"introduce el  numero inicial for")
numero = int(input())

for num in range(1, 11):
    resultado=numero * num
    print(f" {numero} por {num} = {resultado}")

print(f"introduce el  numero inicial while")
numero2 = int(input())

contador = 1
while (contador < 11):
    result=numero2 * contador
    print(f"{numero2} por {contador} = {result}")
    contador += 1


# ss = numero1 * contador for numero2