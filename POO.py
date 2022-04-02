class Coche():
    # Definimos las propiedades de la clase Coche
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    
    # Creamos metodos para definir el comportamiento
    # de los objetos (no son funciones); siempre tienen
    # que llevar el self dentro de los parametros
    
    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
    
    def estado(self):
        print("El coche tiene", self.ruedas, "ruedas. Un ancho de",
              self.anchoChasis, "y un largo de", self.largoChasis)
        
    
# Para crear un objeto salimos de la clase 
# Indicamos la clase a la que pertenece ese objeto

miCoche = Coche()

# Le damos el metodo arrancar al objeto miCoche:

print(miCoche.arrancar(True))

'''Ahora miCoche tiene la propiedad de enmarcha con valor True'''

miCoche.estado()

print("------------------------A continuacion creamos el segundo objeto------------------------")

# Creamos el segundo objeto

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()