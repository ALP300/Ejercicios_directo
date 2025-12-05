'''
Escribir un programa que almacene 
las asignaturas de un curso (por 
ejemplo Matemáticas, Física, Química,
Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha 
sacado en cada asignatura y elimine de
la lista las asignaturas aprobadas. Al
final el programa debe mostrar por 
pantalla las asignaturas que el
usuario tiene que repetir.
'''
cursos=["programacion","calculo","fisica","quimica"]
aprobados=[]
for curso in cursos:
    nota= float(input(f"Por favor ingresa la nota de {curso}: "))
    if nota>=11:
        aprobados.append(curso)

for apro in aprobados:
    cursos.remove(apro)

print("Tienes que repetir: ", cursos)
