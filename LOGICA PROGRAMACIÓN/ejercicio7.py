'''
Contador de dígitos pares e impares:
Solicita un número entero largo, y con 
un bucle determina cuántos dígitos 
son pares y cuántos impares.
'''
def contador_digitos():
    numero=input("Por favor, ingresa el número: ")
    pares=0
    impares=0
    for digito in numero:
        if digito.isdigit():
            if int(digito)%2==0:
                pares+=1
            else:
                impares+=1
    
    print("Dígitos pares: ", pares)
    print(f"Impares {impares}")
    
contador_digitos()