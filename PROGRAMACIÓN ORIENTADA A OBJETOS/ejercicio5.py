'''
Crea una clase Persona con los atributos
nombre y edad (la edad no puede ser negativa).
El nombre debe guardarse con mayúscula inicial. 
Implementa un método cumplir_años() que 
aumente la edad en 1 y un método presentarse() 
que devuelva un mensaje de saludo con su nombre
y edad. Sobrescribe __str__ para mostrar 
algo como Persona(Leo, 23 años).
'''

class Persona:
    def __init__(self,nombre, edad):
        if edad<0:
            raise ValueError("La edad no puede ser negativa")
        self.nombre= nombre
        self.edad= edad
    
    def cumplir_años(self):
        self.edad+=1

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"


p= Persona("leo",22)
p.cumplir_años()
print(p.presentarse())
p1= Persona("pepe",26)
p1.cumplir_años()
print(p1.presentarse())
p2= Persona("Luis",29)
print(p2.presentarse())