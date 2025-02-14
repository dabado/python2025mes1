from class32mes import Mes
import random

Enero=Mes(10, 8)
Enero.nombre="Enero"
print(f"temperatura maxima Enero {Enero.temperatura_maxima}")
print(f"temperatura media Enero {Enero.temperatura_media}")
print(f"temperatura minima Enero {Enero.temperatura_minima}")
Febrero=Mes(14, 10)
Febrero.nombre="Febrero"
print(f"temperatura maxima Febrero {Febrero.temperatura_maxima}")
print(f"temperatura media Febrero {Febrero.temperatura_media}")
print(f"temperatura minima Febrero {Febrero.temperatura_minima}")
print(Enero.temperatura_maxima)
print(Enero)
Marzo=Mes()
meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","novienbre","diciembre")

for nombremes in meses:
    #print(nombremes)
    mes = Mes()
    mes.nombre = nombremes
    mes.temperatura_maxima = random.randint(1, 40)
    mes.temperatura_minima = random.randint(1, 40)
    print(mes)
