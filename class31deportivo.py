from class30coche import Coche
class deportivo(Coche):
    velocidad = 0
    turbo = 20
    def turbo(self):
        self.velocidad += 120 + self.velocidad
        return self.velocidad