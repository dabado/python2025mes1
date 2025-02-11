

datos = "EL murcielago verde vuela"
print(datos[:14])
print(datos[14:20])
print(datos[20:])
print(datos.upper())
print(datos.replace("verde", "Rojo").upper())
print(datos)
verbos=datos.find("vuela")
print(f"verbo usado ",datos[verbos:])
datos=datos.replace(" ", "_")
print(datos)
print(datos[20:].isalpha())
print(datos.isalnum())
print(datos.isdigit())
for i in datos[:]:

    print(i)

print(f"posiciones totales:", len(datos))