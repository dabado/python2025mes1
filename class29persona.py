class Persona:
    nombre = ""
    apellidos = ""
    email = "@"
    anyonacimiento = ""
    pais = ""
    
    
    def __init__(self):
        self.pais = "Espanya"

    def __str__(self):
        return self.nombre + " " + self.apellidos + " año de nacimiento: " + self.anyonacimiento + " email:" + self.email + " pais: " + self.pais
    

    def getNOmbreCompleto(self):
        return self.nombre + " " + self.apellidos
    
    def getNombre(self):
        return self.nombre
    
    def getPasis(self):
        return self.pais
    
    def getAnyoNacimiento(self):
        return self.anyonacimiento
    
    def getEmail(self):
        return self.email
    
    
    def getEdad(self):
        return 2025 - self.anyonacimiento
    