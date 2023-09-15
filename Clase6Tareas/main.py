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

class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None
    def estaVacia(self):
        return  self.cabeza == None
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
    def tamaño(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador +=1
            actual = actual.obtenerSiguiente()
        return contador
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual !=None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado= True
            else:
                actual= actual.obtenerSiguiente()
        return encontrado

"""milista = ListaNoOrdenada()
milista.agregar(25)
milista.agregar(31)
milista.agregar(22)
print(milista.buscar(23))"""