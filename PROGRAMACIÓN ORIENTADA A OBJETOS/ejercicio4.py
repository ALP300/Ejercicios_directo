'''
Crea una clase Circulo que reciba 
un radio mayor a 0. Implementa los
métodos area() y perimetro(), 
ambos redondeados a 2 decimales, 
y una propiedad diametro que retorne
el doble del radio. Sobrescribe __str__ 
para mostrar algo como 
Círculo(radio=5, área=78.54).
'''
import math
class Circulo:
    def __init__(self, radio):
        if radio<=0:
            raise ValueError("El radio debe ser mayor a 0")
        self.radio= radio
    
    def area(self):
        return round(math.pi*(self.radio**2),2)
    
    def perimetro(self):
        return round(2*math.pi*self.radio,2)
c1= Circulo(5)
c2= Circulo(10)
    