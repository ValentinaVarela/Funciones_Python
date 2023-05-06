#FUNCIONES: Ahorrar lineas de codigo, reutilizar codigo, dividir el programa en pequeñas tareas.

#DECLARAR UNA FUNCIÓN:
"""def NombreFuncion(parametro1, parametro2...):
   Conjunto de instrucciones
NombreFuncion(Argumento1, Argumento2.....)"""

#FUNCIÓN SIN PARAMETROS
def DerechosHumanos():
    print("Derecho a la vida\nDerecho a la salud\nDerecho a la educación\nDerecho a la libre expresión\nDerecho a la libertad\nDerecho al libre desarrollo de la personalidad")
DerechosHumanos()

def MayoresdeEdad():
   print("Derecho a morir dignamente\nDerecho al trabajo\nDerecho a una vejez digna\nDerecho a votar")

#FUNCION CON PARAMETROS:
#Declarar una funcion que muestre los derechos humanos y derechos mayores de edad, si la edad es mayor o igual que 18, de lo contrario solo muestre los derechos humanos
def Derechos(Nombre, Edad=23):
   print(f"{Nombre} Tus derechos son: ")
   if Edad >= 18:
      DerechosHumanos()
      MayoresdeEdad()
   else:
      DerechosHumanos()
#Edad = int(input("Ingrese la edad: "))
Derechos("Yulieth", 9)

#FUNCION DIVISION: Divisor es 0 debe arrojar un mensaje de error, de lo contrario muestre el resultado
Divisor = 3
def Division(Dividendo, Divisor):
   if Divisor == 0:
      print("No existe la division por cero")
   else:
      print(f"El cociente es {Dividendo // Divisor}")
Division(20, Divisor)
print(Divisor)

