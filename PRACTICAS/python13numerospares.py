print(f"introduce el  numeroinicial ")
numero1 = int(input())
print(f"introduce el numero final")
numero2 = int(input())

for num in range(numero1, numero2, 1):
    print(num)

print("otro")
for numeros in range(numero1, numero2):
    if (numeros % 2 == 0):
        print(numeros)