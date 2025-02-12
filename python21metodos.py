#print(f"introduce un numero")
#num=int(input())

def positivoOnegativo(num=0):
    if (num == 0 ):
        print(f"el numero {num} es neutro")
    elif (num < 0):
        print(f"el numero {num} es negativo")
    else:
        print(f"el numero {num} es positivo")



def rangoPar(numero1=0, numero2=0):

    numeros = numero1 , numero2
    print("en el rango tenemos los siguientes pares ", numeros)
    for numeros in range(numero1, numero2):
        if (numeros % 2 == 0):
            print(numeros)



def validarMail(mail):
    posicion_arroba=mail.find("@")
    posicion_arroba2=mail.rfind("@")
    if posicion_arroba != posicion_arroba2 or (mail.count("@") > 1):
        print("hay mas de una arroba")
    elif (mail[posicion_arroba:]).startswith("@") == True or (mail[posicion_arroba:]).endswith("@") == True:
        print("si tiene una arroba", mail[posicion_arroba:])
    elif (mail[posicion_arroba2:]).startswith("@") or ((mail[posicion_arroba2:]).endswith("@")):
        print("si tiene una arroba", mail[posicion_arroba2:])
    else:
        print("no he encontrado arroba")


    posicion_punto=mail.find(".") 
    posicion_punto2=mail.rfind(".") 
    extension=mail[posicion_punto + 1 : ] 
    dominio=mail[posicion_arroba + 1 : posicion_punto]
        


    if (mail[posicion_punto:]).startswith(".") :
        print("si tiene un punto", mail[posicion_punto:])
    elif (mail[posicion_punto != posicion_punto2]) or (mail.count(".") != 1):
        print("hay mas de un punto")
    elif (mail[posicion_punto2:]).startswith("."):
        print("si tiene un punto", mail[posicion_punto2:])

    print(f"la extension del dominio es : ", extension.upper())
    print(f"el dominio es {dominio.upper()} con una longitud de dominio de {len(dominio)} digitos ")
    longExtDominio= len(extension)


    if longExtDominio == 3 :
        print(f"es una extension de dominio de tres letras")
    elif longExtDominio == 2 :
        print(f"es una extension de dominio de dos letras")
    else:
        print("la extension del dominio no es correcta")

positivoOnegativo(num=200)
positivoOnegativo(num=0)
positivoOnegativo(num=-100)

print(f"resultados: ", str(positivoOnegativo(2)))
rangoPar(1, 20)
rangoPar(8, 20)
rangoPar(12, 20)
validarMail("david@dbddominio.es")


