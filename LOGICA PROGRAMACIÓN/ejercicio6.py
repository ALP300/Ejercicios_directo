'''
Tablas cruzadas:
Genera la tabla de multiplicar 
del 1 al 12 para los números del
1 al 10. Imprime cada
tabla en bloques separados.
'''
def tabla_multiplicar():
    for num in range(1,11):
        for i in range(1,13):
            print(f"{num} x {i}= {num*i}")
    print()

tabla_multiplicar()