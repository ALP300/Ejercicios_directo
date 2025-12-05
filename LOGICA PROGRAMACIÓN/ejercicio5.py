'''
Suma condicional de múltiplos:
Pide un número N y suma solo los múltiplos 
de 3 o 5 hasta N. Muestra la suma y los
múltiplos encontrados.
'''
def suma_multiplos():
    n= int(input("Por fi, ingresa el valor de N: "))
    suma=0
    multiplos=[]
    for i in range(2, 100, 2):
        if i%3==0 or i%5==0:
            suma+=i
            multiplos.append(i)
    
    print(f"Múltiplos de 3 o 5 {multiplos}")
    print(f"La suma es:  {suma}")
    
    
suma_multiplos()