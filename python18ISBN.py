print(f"introduce el ISBN")
#     8441513929
numero = input()

if len(numero) == 10 :
    print("tiene 10 digitos")
else:
    print("numero menor de 10 digitos")

lista=[]
sum = 0

for i in numero:
    sum = sum + int(i)
    lista.append(int(i))

    listatotal = len(lista)    
    while listatotal > 0 :
        letra = i
        print(letra)
        ejecucion = letra * int(listatotal)
        listatotal -= 1
 
        print(letra , listatotal)
    
#print(f"suma: " ,sum)




