from random import randint
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
class listaEnlazadaOrdenada():
    def __init__(self):
        self.cabeza = None
    def estaVacia(self):
        return self.cabeza == None
    def agregarNodo(self, item):
        temp = Nodo(item)
        actual = self.cabeza
        previo = None

        while actual is not None and actual.consultarDato() < item:
            previo = actual
            actual = actual.consultarSiguiente()

        if previo is None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            previo.asignarSiguiente(temp)
            temp.asignarSiguiente(actual)
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
        print("None")
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
    def generarMilNumeros(self):
        for i in range(1000):
            self.agregarNodo(randint(5,300))
miListaOrdenada1 = listaEnlazadaOrdenada()
miListaOrdenada1.generarMilNumeros()
miListaOrdenada1.mostrarLista()