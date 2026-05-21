class personaje:

    def  __init__(self):
        self.NOMBRE = "nombre por defecto"
        self.TIPO =  " tipo por defecto"

    def Cantar(self):
        print("El personaje llamado" + self.NOMBRE + " canta ")

class Druida(personaje):

    def __init__(self, nombre, nivel):
        self.NOMBRE = nombre
        self.TIPO = "DRUIDA"
        self.NIVEL_DRUIDA = nivel

    def InventarPocion(self):
        print("El druida llamado" +self.NOMBRE + "inventa una posicion.")

pygamix = Druida("Pygamix", 5)
pygamix.Cantar()
pygamix.InventarPocion()


# Definicion de la clase Vehiculo
class Vehiculo:

    # Constructor de la clase Vehiculo
    def __init__(self, matricula, color, numeroPuertas):
        self.MATRICULA = matricula
        self.COLOR = color
        self.NUMERO = numeroPuertas
        self.AVANZA = False
        print("Construccion de un vehiculo :" + self.MATRICULA)

    # Metodo Avanzar
    def Avanzar(self):
        self.AVANZA = True
        print(self.MATRICULA + "avanza.")

    # Metodo Detenerse
    def Detenerse(self):
        self.AVANZA = False
        print(self.MATRICULA + "se detiene.")

# Construccion de una primera instancia
vehiculo1 = Vehiculo("AR123", "rojo", 3)

# Construccion de una segunda instancia
vehiculo2 = Vehiculo("FR456", "verde", 5)

# El primer vehiculo avanza
vehiculo1.Avanzar()

# El primer vehiculo se detiene
vehiculo1.Detenerse()


# en la linea (1,3) es para iniciar el programa
# en la linea (1,3) es para iniciar el programa
# en la linea (4,10) es para crear el vehiculo la matricula el color y las puertas
# en la linea (11,15) espara que el vehicul avanse 
# en la linea (16,20) es para que el vehiculo de detenga
# en la linea (22,33) es para la cnstruccion del vehiculo 1 y la construccion del vehiculo 2 
# es para que el carro 1 avanse y se detenga
# definicion de la clase Vehiculo