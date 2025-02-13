

enteros = [10,20,85,93,39,48,59,68,72]
string = ["David","paco","juan","angel","antonio","ana","lucia","señor mayor","vegestorio"]

print(enteros[2])
print(string[0])
print(string[0] + str(enteros[0]))

print(len(enteros))
print(len(string))
print("David" in string)
string.append("casimiro")
print(string[-1])
print(string[2])
string.insert(2, "candido")
print(string[2])
string.remove("candido")
print("david" in string)
string.pop(2)
#string.clear()
string.sort(reverse=True)
for posicion in range(len(string)):
    print(str(posicion) + "=" + string[posicion]) 

enteros.sort( reverse=True)
for i in range(len(enteros)):
    print(enteros[i])

