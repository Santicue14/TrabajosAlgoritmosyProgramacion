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

class Triangulo():
    lados=[]
    mayor=-10000
    def __init__(self,lado1,lado2,lado3):
        self.lados.append(lado1)
        self.lados.append(lado2)
        self.lados.append(lado3)
    def evaluarMayorLado(self):
        for i in range(len(self.lados)):
            if self.lados[i] > self.mayor:
                self.mayor = self.lados[i]
        print(f"El mayor lado es {self.mayor}")
    def evaluarTipo(self):
        if self.lados[0] == self.lados [1] == self.lados[2]:
            print("El triangulo es equilátero")
        elif self.lados[0] == self.lados[1] or self.lados[0] == self.lados[2] or self.lados[1] == self.lados[2]:
            print("El triángulo es isóceles")
        else:
            print("El triángulo es escaleno")

triangulito = Triangulo(1,2,3)
triangulito.evaluarMayorLado()
triangulito.evaluarTipo()

#Actividad 4 clase 4
class Calculadora():
    num = []
    def __init__(self):
        for i in range(2):
            while True:
                num = input(f"Ingrese su {i+1} número")
                if verificarInputsNumeros(num):
                    self.num.append(float(num))
                    break
                else:
                    print("Ingrese un numero válido")
    def calculos(self):
        suma = self.num[0] + self.num [1]
        resta = self.num[0] - self.num [1]
        multi = self.num[0] * self.num [1]
        print(f'{self.num[0]} + {self.num[1]} = {suma}\n{self.num[0]} - {self.num[1]} = {resta}\n{self.num[0]} * {self.num[1]} = {multi}')
        try:
            division = self.num[0] / self.num[1]
            print(f'{self.num[0]} / {self.num[1]} = {division:.2f}')
        except ZeroDivisionError:
            print("No es posible dividir por 0")


calcu = Calculadora()
calcu.calculos()
