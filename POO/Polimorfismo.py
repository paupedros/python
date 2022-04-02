class Coche():
    
    def desplazamiento(self):
        print("Me he desplazado utilizando cuatro ruedas")
        
        
class Moto():
    
    def desplazamiento(self):
        print("Me he desplazado utilizando dos ruedas")
        

class Camion():
    
    def desplazamiento(self):
        print("Me he desplazado utilizando seis ruedas")
        
        

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
    
    
miCamion = Coche()

desplazamientoVehiculo(miCamion)