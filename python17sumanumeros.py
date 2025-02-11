print(f"introduce el texto numerico")
numero = input()
lista=[]
sum = 0
for i in numero:
    sum = sum + int(i)
    lista.append(int(i))
print(lista)
print(f"suma: " ,sum)