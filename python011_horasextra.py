print(f"introduce horas trabajadas")
horas = int(input())
print(f"introduce precio de la hora trabajada")
precioHora = int(input())
print(f"introduce los kilometros")
kilometros = int(input())


horasSemanales = 40
salarioBase = horasSemanales * precioHora


if horas <= horasSemanales :
    horasExtra = 0
elif horas > horasSemanales:
    horasExtra = (horas  - horasSemanales ) * (precioHora + 2)   

salarioTotal = salarioBase + horasExtra


if kilometros <= 100:
    dietas = "LOCALES"
elif kilometros >= 101 and kilometros <= 500:
    dietas = "PROVINCIALES"
elif kilometros > 500:
    dietas = "NACIONALES"



if salarioTotal <= 250:
    retenciones = 0
elif salarioTotal >= 251 and precioHora <= 600:
    retenciones = 20
elif salarioTotal >= 600:
    retenciones = 40

print("------------------------------------------------------------------------")
print(f"dietas:     {dietas}                   retencion:  {retenciones} %")
print("--------")
print(f"salario Base :      {salarioBase} euros     Horas Extra :   {horasExtra} euros")
print("--------")
print(f"el salario total es :   {salarioTotal} euros ")
print("                             --------")
print("                             --------")



