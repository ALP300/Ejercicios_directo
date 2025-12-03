'''
Crea una clase CuentaBancaria 
con un titular y un saldo inicial 
de 0. Implementa depositar(monto) 
y retirar(monto) con validación 
para montos negativos y para
evitar retiros mayores al saldo,
retornando mensajes adecuados. 
Sobrescribe __str__ para mostrar 
el titular y el saldo actual.
'''
class CuentaBancaria:
    def __init__(self, titular):
        self.titular= titular
        self.saldo= 0
    
    def depositar(self,monto):
        if monto<=0:
            return "El monto debe ser positivo"
        self.saldo+=monto
        return f"Depósito exitoso {monto} y el final {self.saldo}"

c1= CuentaBancaria("Leo")
print(c1.depositar(200))