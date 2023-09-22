class Pila:
    # Definimos el contructor   
    def __init__(self):
        # Inicializamos una 'pila vacía', el elemento contenedor es del
        # tipo de dato lista, donde se irán apilando los elementos.  
        self.lista = []
    
    # Método  que agrega un nuevo elemento a la pila (lista)    
    def apilar(self,item):
        self.lista.append(item)
        
    # Método  que quita el último elemento ingresado de la pila (lista)
    def desapilar(self):
        if self.vacia():
            print("No se puede desapilar la lista está vacía")
        else:
            print(f"Elemento desapilado -> {self.lista.pop()} ")
         
    # Método  que controla si la lista está vacía
    def vacia(self):
        if len(self.lista)==0:           
            return True
        else:           
            return False
    
    def mostrar(self):
        for i in self.lista[::-1]:
            print(f"[{str(i):^10}]")
        print()


class Cola:
    """ Representa a una cola, con operaciones de encolar y desencolar.
        El primero en ser encolado es también el primero en ser desencolado.
    """
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.lista_cola=[]
    
    def encolar(self, x):
        ''' Agrega el elemento x como último de la cola.  '''
        self.lista_cola.append(x)
    
    def desencolar(self):
        ''' Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía envia un mensaje de cola vacia. '''
        
        if self.es_vacia():
            print("La cola está vacía")
        else:
            self.lista_cola.pop(0)
           
    def es_vacia(self):
        ''' Devuelve True si la cola esta vacía, False si no. '''
        return self.lista_cola == []
    
    def mostrar(self):        
        print(self.lista_cola)
     




