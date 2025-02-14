class Mes:
    nombre=""
    temperatura_maxima=int("10")
    temperatura_minima=int("6")
    temperatura_media=""
    def __init__(self, temperatura_maxima=temperatura_maxima, temperatura_minima=temperatura_minima):
        self.temperatura_maxima = temperatura_maxima
        self.temperatura_minima = temperatura_minima
        temperatura_media = (int(self.temperatura_maxima) + int(self.temperatura_minima)) / 2
        self.temperatura_media = temperatura_media
        
    def __str__(self):
        #print(f"Temperatura maxima: {self.temperatura_maxima} entre temperatura minima {self.temperatura_minima} , es igual a temperatura_media")
        return self.nombre + " maximo " + str(self.temperatura_maxima) + " minimo " + str(self.temperatura_minima)  + " media " + str(self.temperatura_media)
    