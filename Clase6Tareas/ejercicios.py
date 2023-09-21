class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
    def obtenerDato(self):
        return self.dato
    def obtenerSiguiente(self):
        return self.siguiente
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
class listaNoOrdenada:
    def __init__(self):
        self.cabeza = None
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    def buscar(self,item):
        actual = self.cabeza
        loencontro = False
        while actual != None and not loencontro:
            if actual.obtenerDato() == item:
                loencontro = True
            else:
                actual = actual.obtenerSiguiente()
        return loencontro
    def tamaño(self):
        actual = self.cabeza
        contador_tamaño = 0
        while actual != None:
            contador_tamaño += 1
            actual = actual.obtenerSiguiente()
        return contador_tamaño
    def estaVacia(self):
        return self.cabeza == None
    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if actual != None:
            print(f'{item} borrado con exito')
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
        else:
            print(f"{item} no encontrado!")
    def verLista(self):
        actual = self.cabeza
        print ("Cabeza",end="->")
        while actual != None:
            print(actual.obtenerDato(),end="->")
            actual = actual.obtenerSiguiente()
    def anexar(self,item):
        temp = Nodo(item)
        actual = self.cabeza
        previo = None
        while actual != None:
            previo = actual
            actual = actual.obtenerSiguiente()
        if previo == None:
            self.agregar(item)
        else:
            previo.asignarSiguiente(temp)

milistaNoOrdenada = listaNoOrdenada()
print(milistaNoOrdenada.estaVacia())
milistaNoOrdenada.agregar(40)
milistaNoOrdenada.agregar(90)
milistaNoOrdenada.agregar(50)
print(milistaNoOrdenada.verLista())
milistaNoOrdenada.remover(50)
milistaNoOrdenada.remover(70)
milistaNoOrdenada.anexar(70)
print(milistaNoOrdenada.verLista())