
def validacionesISBN(isbn=0000000000):
    
    longitud = len(isbn)
    if (longitud != 10):
        print("El número ISBN debe tener 10 caracteres")
    elif (isbn.isdigit() == False):
        print("El número ISBN debe contener solo números")
    else:
        suma = 0
        for i in range(longitud):
            letra = isbn[i]
            numero = int(letra)
            operacion = numero * (i + 1)
            suma = suma + operacion
        if (suma % 11 == 0):
            print("El numero isbn " + isbn + " es CORRECTO")
        else:
            print("El número ISBN NO ES CORRECTO")
        print("Fin de programa")


def letraDni(numDNI):
        DNILetra = numDNI - int(numDNI / 23 )* 23
        print(f"El resultado de la operacion es : {DNILetra}")

        if DNILetra == 0 :
            print(f"la letra es T")
        elif DNILetra == 1 :
            print(f"la letra es R")
        elif DNILetra == 2 :
            print(f"la letra es W ")
        elif DNILetra == 3 :
            print(f"la letra es A, el DNI completo es {numDNI}-A")
        elif DNILetra == 4 :
            print(f"la letra es G, el DNI completo es {numDNI}-G")
        elif DNILetra == 5 :
            print(f"la letra es M, el DNI completo es {numDNI}-M")
        elif DNILetra == 6 :
            print(f"la letra es Y")
        elif DNILetra == 7 :
            print(f"la letra es F")
        elif DNILetra == 8 :
            print(f"la letra es P")
        elif DNILetra == 9 :
            print(f"la letra es D")
        elif DNILetra == 10 :
            print(f"la letra es X")
        elif DNILetra == 11 :
            print(f"la letra es B")
        elif DNILetra == 12 :
            print(f"la letra es N")
        elif DNILetra == 13 :
            print(f"la letra es J")
        elif DNILetra == 14 :
            print(f"la letra es Z")
        elif DNILetra == 15 :
            print(f"la letra es S")
        elif DNILetra == 16 :
            print(f"la letra es Q")
        elif DNILetra == 17 :
            print(f"la letra es V")
        elif DNILetra == 18 :
            print(f"la letra es H")
        elif DNILetra == 19 :
            print(f"la letra es L")
        elif DNILetra == 20 :
            print(f"la letra es C")
        elif DNILetra == 21 :
            print(f"la letra es K")
        elif DNILetra == 22 :
            print(f"la letra es E")
        elif DNILetra == 23 :
            print(f"la letra es T")
        else:
            print("el valor no es correcto")
            
