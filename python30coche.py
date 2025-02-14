from class30coche import Coche

cocheDavid = Coche()
print(cocheDavid.estado)
cocheDavid.acelerar()
print(cocheDavid.velocidad)
cocheDavid.arrancar()
print(cocheDavid.estado)
cocheDavid.acelerar()
cocheDavid.acelerar()
cocheDavid.frenar()
print(cocheDavid.estado)
cocheDavid.detener()
print(cocheDavid.estado)
print(cocheDavid.velocidad)


class deportivo(Coche):
    velocidad = 100
    turbo = 20


DAvidDeportivo = deportivo()
deportivo.arrancar
deportivo.acelerar
print(deportivo.velocidad)