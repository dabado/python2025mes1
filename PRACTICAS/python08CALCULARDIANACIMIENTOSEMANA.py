from math import  trunc

print("introduce un numero dia")
numDia=int(input())
print("introduce un numero mes")
numMes=int(input())
print("introduce un numero año")
numAnual=int(input())



if numMes == 1 :
    numMes = 13
    numAnual = numAnual - 1
elif numMes == 2 :
    numMes = 14
    numAnual = numAnual - 1
else:
    print(f"continuamos")

resultado = "numMes/numDia/numAnual"
print(resultado)


ResultadoMultiplicar = trunc((numMes + 1)* 3 / 5)
print(f"1 _ el resultado de multiplicar es : {ResultadoMultiplicar}")
ResultadoDividirAnualentreCuatro = trunc(numAnual // 4)
print(f"2 _ el resultado de dividir el año entre cuatro es : {ResultadoDividirAnualentreCuatro}")
ResultadoDividirAnualentreCien = trunc(numAnual // 100)
print(f"3 _ el resultado de dividir el año entre cien es : {ResultadoDividirAnualentreCien}")
ResultadoDividirAnualentreCuatrocientos = trunc(numAnual // 400)
print(f"4 _ el resultado de dividir el año entre cuatrocientos es : {ResultadoDividirAnualentreCuatrocientos}")
ResultadoSumatorio = trunc((numDia + (numMes * 2 ) + numAnual + ResultadoMultiplicar + ResultadoDividirAnualentreCien) - (ResultadoDividirAnualentreCien + (ResultadoDividirAnualentreCuatro + 2)))
print(f"5 _ el resultado de Sumatorio : {ResultadoSumatorio}")
ResultadoSumatorioEntreSiete = trunc(ResultadoSumatorio / 7)
print(f"6 _ el resultado de Sumatorio entre siete: {ResultadoSumatorioEntreSiete}")
ResultadoSumatorioMenosSumatorioEntreSietePorsiete = trunc((ResultadoSumatorio - ResultadoSumatorioEntreSiete) * 7)
Resultado = ResultadoSumatorioMenosSumatorioEntreSietePorsiete
print(f"7 _ ResultadoSumatorio Menos SumatorioEntreSiete Por siete es : {ResultadoSumatorioMenosSumatorioEntreSietePorsiete}")
diasDeSemana = ""
if Resultado == 0:
    print(f"dia de la semana SABADO", Resultado)
elif Resultado == 1:
    print(f"dia de la semana DOMINGO", Resultado)

elif Resultado == 2:
    print(f"dia de la semana LUNES", Resultado)

elif Resultado == 3:
    print(f"dia de la semana MARTES", Resultado)

elif Resultado == 4:
    print(f"dia de la semana Miercoles", Resultado)

elif Resultado == 5:
    print(f"dia de la semana JUEVES", Resultado)

elif Resultado == 6:
    print(f"dia de la semana VIERNES", Resultado)
else:
    print(f"revisa las operaciones")
