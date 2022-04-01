class Coche():
    # Definimos las propiedades de la clase Coche
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    
    
    # Creamos metodos para definir el comportamiento
    # de los objetos (no son funciones); siempre tienen
    # que llevar el self dentro de los parametros
    
    def arrancar(self):
        self.enmarcha = True    # == miCoche.enmarcha = True
        
    '''Lo que hace este metodo es cambiar el valor de la
    propiedad enmarcha a True'''
    
    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    
# Para crear un objeto salimos de la clase 
# Indicamos la clase a la que pertenece ese objeto

miCoche = Coche()

# Para ver una propiedad del objeto utilzamos 
# la nomencaltura del punto. Ejemplo:

print("El largo de mi coche es: ",miCoche.largoChasis)

# Le damos el metodo arrancar al objeto miCoche:

miCoche.arrancar()

'''Ahora miCoche tiene la propiedad de enmarcha con valor True'''

print(miCoche.estado())