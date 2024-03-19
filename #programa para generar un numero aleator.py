#programa para generar un numero aleatorio en python
import random
#la funcion input() capatura de datos desde el teclado
# como asi fuera una cadena de texto(string)
a= input("limite inferior")
b= input("limite superior")

#convertir a y b en enteros
a= int(a)
b= int(b)
respuesta= random.randint(a,b)
print(respuesta) 