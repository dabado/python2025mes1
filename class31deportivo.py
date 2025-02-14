from class30coche import Coche
class deportivo(Coche):
    velocidad = 0
    turbo = 20

    def __init__(self):
        super().__init__()
        self.marca="ferrari"

    def Velocidad_Maxima(self): 
          print(f"la velocidad maxima del deportivo {self.marca} es {super().Velocidad_Maxima()} mas la del deportivo 100")
          velocidadDeportivo= super().Velocidad_Maxima() 
          return velocidadDeportivo + 100
    
    def turbo(self):
        self.velocidad += 80 
        print(f"activado el turbo !! {self.velocidad} {self.marca}  ")

    def acelerar(self):
        self.velocidad +=60
        return self.velocidad

