class Nodo():
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
    def consultarDato(self):
        return self.dato
    def consultarSiguiente(self):
        return self.siguiente
    def asignarSiguiente(self,nuevoSiguiente):
        self.siguiente = nuevoSiguiente

class ListaEnlazada():
    def __init__(self):
        self.cabeza = None
    def estaVacia(self):
        return self.cabeza == None
    def agregarNodo(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.consultarSiguiente()
        return contador
    def mostrarLista(self):
        print(f'Cabeza',end="->")
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(f'{actual.consultarDato()}',end="->")
                actual = actual.consultarSiguiente()
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.consultarDato() == item:
                encontrado = True
            else:
                actual = actual.consultarSiguiente()
        return encontrado
    def eliminarElementos(self):
        actual = self.cabeza
        previo = None
        encontrado = False
        itempeliminar = input("Ingrese el valor a eliminar")
        if actual is not None and actual.consultarDato() == itempeliminar:
            self.cabeza = actual.consultarSiguiente()
            actual = None
            encontrado = True
            print(f'{itempeliminar} eliminado correctamente')
        while not encontrado and actual != None:
            if actual.consultarDato() == itempeliminar:
                encontrado = True
            else:
                previo = actual
                actual = actual.consultarSiguiente()
        if not encontrado:
            print(f'{itempeliminar} no encontrado!')
        elif actual != None:
            previo.asignarSiguiente(actual.consultarSiguiente())
            actual= None
            print(f'{itempeliminar} eliminado correctamente')
    def anexar(self,item):
        temp = Nodo(item)
        previo = None
        actual = self.cabeza
        while actual != None:
            previo = actual
            actual = actual.consultarSiguiente()
        if actual == None:
            previo.asignarSiguiente(temp)
            temp.asignarSiguiente(actual)

"""#Lista de colores
miLista1= ListaEnlazada()
miLista1.agregarNodo("Blanco")
miLista1.agregarNodo("Negro")
miLista1.agregarNodo("Azul")
miLista1.agregarNodo("Oro")
miLista1.agregarNodo("Rojo")
miLista1.agregarNodo("Gris")
print("Lista de colores: ",end="")
print(f'{miLista1.mostrarLista()}')
miLista1.eliminarElementos()
miLista1.eliminarElementos()
print("Lista actualizada: ",end="")
print(f'{miLista1.mostrarLista()}')

#Lista de nombres
miLista2= ListaEnlazada()

miLista2.agregarNodo("Juan")
miLista2.agregarNodo("Santiago")
miLista2.agregarNodo("Raúl")
miLista2.agregarNodo("Andrea")
miLista2.agregarNodo("Victoria")
miLista2.agregarNodo("Luis")
print("Lista de nombres: ",end="")
print(f'{miLista2.mostrarLista()}')
miLista2.eliminarElementos()
miLista2.eliminarElementos()
print("Lista actualizada: ",end="")
print(f'{miLista2.mostrarLista()}')

#Numeros random entre 1990 y 2045
from random import randint
miLista3= ListaEnlazada()
miLista3.agregarNodo(str(randint(1990,2045)))
miLista3.agregarNodo(str(randint(1990,2045)))
miLista3.agregarNodo(str(randint(1990,2045)))
miLista3.agregarNodo(str(randint(1990,2045)))
miLista3.agregarNodo(str(randint(1990,2045)))
print("Lista de numeros random: ",end="")
print(f'{miLista3.mostrarLista()}')
miLista3.eliminarElementos()
miLista3.eliminarElementos()
print("Lista actualizada: ",end="")
print(f'{miLista3.mostrarLista()}')

#Anexar nuevo color
print(f'Anexando un nuevo color')
miLista1.anexar("Amarillo")
print(miLista1.mostrarLista())

#Mostrar tamaño lista numeros
print(f'El tamaño de la lista de números es: {miLista3.tamano()}')"""

class listaEnlazadaOrdenada():
    def __init__(self):
        self.cabeza = None
    def estaVacia(self):
        return self.cabeza == None
    def agregarNodo(self,item):
        temp = Nodo(item)
        actual = self.cabeza
        previo = None
        while actual != None or actual.consultarDato() < temp :
            previo = actual
            actual = actual.consultarSiguiente()
        if previo == None:
            self.cabeza = temp
            temp.asignarSiguiente(actual)
        elif actual < temp:
            previo.asignarSiguiente(temp)
            actual = temp

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.consultarSiguiente()
        return contador
    def mostrarLista(self):
        print(f'Cabeza',end="->")
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(f'{actual.consultarDato()}',end="->")
                actual = actual.consultarSiguiente()
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual < item or actual != None:
            if actual.consultarDato() == item:
                encontrado = True
            else:
                actual = actual.consultarSiguiente()
        return encontrado
    def eliminarElementos(self):
        actual = self.cabeza
        previo = None
        encontrado = False
        itempeliminar = input("Ingrese el valor a eliminar")
        if actual is not None and actual.consultarDato() == itempeliminar:
            self.cabeza = actual.consultarSiguiente()
            actual = None
            encontrado = True
            print(f'{itempeliminar} eliminado correctamente')
        while not encontrado and actual != None:
            if actual.consultarDato() == itempeliminar:
                encontrado = True
            else:
                previo = actual
                actual = actual.consultarSiguiente()
        if not encontrado:
            print(f'{itempeliminar} no encontrado!')
        elif actual != None:
            previo.asignarSiguiente(actual.consultarSiguiente())
            actual= None
            print(f'{itempeliminar} eliminado correctamente')

miListaOrdenada1 = listaEnlazadaOrdenada()
miListaOrdenada1.agregarNodo(25)
miListaOrdenada1.agregarNodo(30)
miListaOrdenada1.agregarNodo(2)
miListaOrdenada1.agregarNodo(223312)
miListaOrdenada1.agregarNodo(23123124)
miListaOrdenada1.mostrarLista()