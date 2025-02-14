class Coche:
    marca = "Clio"
    modelo = ""
    velocidad = 0
    estado = False


    def Velocidad_Maxima(self): 
        print(f"la velocidad maxima del coche {self.marca} es 140 ")
        return 140
    
    def acelerar(self):
        if (self.estado == False):
            print("El coche no está arrancado {self.marca}.  Debe arrancar antes")
        else:
            self.velocidad += 20
        print("Velocidad actual " + str(self.velocidad))

    def frenar(self):
        if (self.velocidad == 0):
            print("El coche está detenido")
        else:
            self.velocidad -= 10
        print("Velocidad actual " + str(self.velocidad))

    def arrancar(self):
        self.estado = True
        print("Coche arrancado")

    def detener(self):
        self.estado = False
        self.velocidad = 0
        print("Coche detenido")