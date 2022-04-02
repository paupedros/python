class Coche():
    
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
    
    
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar!!!"
        
        elif(self.__enmarcha == False):
            return "No se ha hecho el chequeo debido a que el coche no esta en marcha"
        
        else:
            return "El coche está parado"
        
    
    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Un ancho de",
              self.__anchoChasis, "y un largo de", self.__largoChasis)
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "Cerradas"
        
        if(self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "Cerradas"):
            return True
        return False
 
miCoche = Coche()

print(miCoche.arrancar(True))

miCoche.estado()

print("------------------------A continuacion creamos el segundo objeto------------------------")

miCoche2 = Coche()

print(miCoche2.arrancar(False))

miCoche2.estado()