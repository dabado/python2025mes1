from libreria25validaciones import validacionesISBN, letraDni

print(f"introduce el ISBN")
#     8441513929
numero = input()
validacionesISBN(numero)
print(f"introduce el ISBN desde codigo :")
validacionesISBN("8441513929")

print(f"introducir DNI sin letra")
numDNI=int(input())
letraDni(numDNI)
print(f"introducir DNI sin letra desde codigo")
letraDni(50203667)