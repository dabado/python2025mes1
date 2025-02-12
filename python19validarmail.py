print(f"introduce el mail")
mail = input()
posicion_arroba=mail.find("@")
posicion_arroba2=mail.rfind("@")
if posicion_arroba != posicion_arroba2:
    print("hay mas de una arroba")

posicion_punto=mail.find(".") 
extension=mail[posicion_punto + 1 : ] 
dominio=mail[posicion_arroba + 1 : posicion_punto]
    
if (mail[posicion_arroba:]).startswith("@"):
    print("si tiene una arroba", mail[posicion_arroba:])

if (mail[posicion_punto:]).startswith("."):
    print("si tiene un punto", mail[posicion_punto:])

print(f"la extension del dominio es : ", extension.upper())
print(f"el dominio es ", dominio.upper())
longExtDominio= len(extension)


if longExtDominio == 3 :
    print(f"es una extension de dominio de tres letras")
elif longExtDominio == 2 :
    print(f"es una extension de dominio de dos letras")
else:
    print("la extension del dominio no es correcta")






