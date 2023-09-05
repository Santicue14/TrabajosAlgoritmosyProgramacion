#Funciones varias para verificar
import array


def verificarInputsNumeros(numero):
    try:
        float(numero)
        return True
    except ValueError as e:
        return False
def verificarInputsStrings(string):
    if len(string) > 0:
        return True
    else:
        return False
#Actividad 1 Clase 4
class Alumno():
    nombre= None
    nota= None
    def pedirNombre(self):
        while True:
            asknombre = input("Ingrese su nombre")
            if verificarInputsStrings(asknombre):
                self.nombre= asknombre.capitalize()
                break
            else:
                print("Ingrese un nombre válido")
    def pedirNota(self):
        while True:
            asknota = input("Ingrese la nota del alumno")
            if verificarInputsNumeros(asknota):
                self.nota = int(asknota)
                break
            else:
                print("Ingrese una nota válida")
    def evaluarNota(self):
        return self.nota >=4
alumno1 = Alumno()
alumno1.pedirNombre()
alumno1.pedirNota()
print(f'El alumno {alumno1.nombre} aprobó? {alumno1.evaluarNota()}')

#Actividad 2 Clase 4
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def verificarMayor(self):
        if self.edad >= 18:
            return "es mayor de edad"
        else:
            return "no es mayor de edad"

personita = Persona("Santiago",18)
print(f'{personita.nombre} {personita.verificarMayor()}')

#Actividad 3 clase 4

def Triangulo():
    lados = ['','','']
    menor = None
    for i in range(len(lados)):
        while True:
            lado = input('Ingrese el lado {i+1}')
            if verificarInputsStrings(lado):
                lados[i] = int(lado)
                for j in range(len(lados)):
                    if menor > lados[i]:
                        

