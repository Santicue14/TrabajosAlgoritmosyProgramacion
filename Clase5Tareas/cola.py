class cola :
    def __init__(self):
        self.clientes = []
    def encolar(self, x):
        self.clientes.append(x)
        print(f'Cliente {x} agregado, cola actualizada: {self.clientes}')
    def es_vacia(self):
        return len(self.clientes) == 0
    def desencolar(self):
        print(f'Cliente {self.clientes.pop(0)} atendido, cola actualizada {self.clientes}')
    def mostrar(self):
        print(f'Turnos restantes ({len(self.clientes)}): {self.clientes}')
miCola = cola()
miCola.encolar("Santiago")
miCola.encolar("Cuevas")
miCola.encolar("Ariel")
miCola.encolar("Baldini")
miCola.encolar("Jamaica")
miCola.encolar("Cristobal")
miCola.encolar("Returno")
print(f'La cola está vacía: {miCola.es_vacia()}')
miCola.desencolar()
miCola.mostrar()