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

"""class ListaNoOrdenada:
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
    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual!=None:
            if actual.obtenerDato() == item and actual.obtenerDato() != None:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
                print(f'Se borró el {item} exitosamente!')
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
        else:
            print(f"El valor {item} para remover no existe")

    def ver(self):
        print("Cabeza",end = "->")
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end ="->")
                actual = actual.obtenerSiguiente()
        print("None")
    def anexar(self,itemnuevo):
        temp = Nodo(itemnuevo)
        actual = self.cabeza
        previo = None
        while actual != None:
            previo = actual
            actual = actual.obtenerSiguiente()
        if previo == None:
            self.agregar(temp)
        else:
            temp = Nodo(itemnuevo)
            previo.asignarSiguiente(temp)
    def buscador(self,indice): #Busca el indice que necesito (HACER PENDIENTE)
        return

milista = ListaNoOrdenada()
milista.ver()
milista.agregar(25)
milista.agregar(31)
milista.agregar(22)
milista.agregar(22)
milista.remover(22)
milista.remover(23)
milista.anexar(60)
milista.ver()"""
class ListaOrdenada:
    def __init__(self):
        self.cabeza = None
    def estaVacia(self):
        return self.cabeza == False
    def tamaño(self):
        actual= self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.obtenerSiguiente()
        return contador
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
            if previo == None:
                actual = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() ==  item:
                encontrado = True
            else:
                if actual.obtenerDato() > item:
                    detenerse = True
            return
    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse  = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        temp = Nodo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)
    def ver(self):
        print("Cabeza",end="->")
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(actual.dato,end="->")
                actual= actual.obtenerSiguiente()
        print("None")

milistaordenada = ListaOrdenada()
milistaordenada.agregar(35)
milistaordenada.agregar(21)
milistaordenada.agregar(45)
milistaordenada.ver()