"""class miPila:
    def __init__(self):
        self.lista = []
    def Apilar(self,unObjeto):
        self.lista.append(unObjeto)
    def estaVacia(self):
        return len(self.lista) == 0
    def Desapilar(self):
        if self.estaVacia():
            print("La pila está vacia, no se puede desapilar!")
        else:
            print(f"Se desapiló el último objeto: {self.lista.pop()}\nLa lista quedó así {self.lista}")
    def tamañoPila(self):
        if not self.estaVacia():
            return len(self.lista)
        else:
            return "la pila está vacía"
    def limpiarPila(self):
        self.lista.clear()
        print("La lista fue borrada exitosamente")
pila= miPila()
print(f'La pila está vacía? {pila.estaVacia()}')
pila.Desapilar()
pila.Apilar("Campera")
pila.Apilar("Remera")
pila.Apilar("Pantalón")
print(f'La pila está vacía? {pila.estaVacia()}')
pila.Desapilar()
print(f"El tamaño de la pila es de {pila.tamañoPila()}")
pila.limpiarPila()
print(f"El tamaño de la pila es de: {pila.tamañoPila()}")"""
#Solicitar al usuario que cargue 10 elementos del tipo string() y despues vamos vaciándola
def verificarInputsStrings(string):
    if len(string) > 0:
        return True
    else:
        return False
def verificarInputsNumeros(numero):
    try:
        numero = int(numero)
        
        return True
    except ValueError as e:
        return False
"""class listaNombres:
    lista = []
    def pedirNombres(self): #Opción 1: esta opción solicita el nombre cada vez que el usuario quiera ingresar uno
        while True:
            nombre = input(f"Ingrese el nombre")
            if verificarInputsStrings(nombre):
                self.lista.append(nombre.capitalize()) #Capitalizo el nombre y lo agrego al final de la lista
                print(f"Nombre cargado con exito!\nLista actualizada {self.lista}")
                break
            else:
                print("El nombre no es válido") #Si el nombre no es un string válido, procede a solicitarlo de vuelta.
    def desapilar(self): #Opción 2, esta opción lo que hace es quitar el último valor ingresado
        if len(self.lista) == 0: #Valida si el largo de largo de la lista es 0, si es así imprime que la lista está vacía
            print("La lista está vacía")
        else:
            self.lista.pop()
            print(f"Se vació un elemento, la lista actualizada es: {self.lista}") #Imprime la lista actualizada ya sin el ultimo valor
    def imprimirNombres(self): #Opción 3, esta opción imprime los nombres ingresados en la lista
        if len(self.lista) == 0: #Valida si el largo de largo de la lista es 0, si es así imprime que la lista está vacía
            print("La lista está vacía")
        else:
            print(self.lista)
    def listaInvertida(self): #Opción 4, esta opción imprime la lista pero de manera invertida
        self.listainv = self.lista[::-1] #Creo la variable de la lista invertida
        print(f"La lista invertida es: {self.listainv}")
    def Menu(self): 
        while True:
            print("1. Apilar nombre\n2. Desapilar nombre\n3. Consultar nombres\n4. Imprimir lista invertida\n5. Salir")
            opcionElegida = input("Ingrese su opción elegida")
            if verificarInputsNumeros(opcionElegida): #Válido si la opcion ingresada es un entero
                opcionElegida = int(opcionElegida)
                if 1 <= opcionElegida <= 4: #Valido si la opción ingresada está en el rango de opciones
                    if opcionElegida == 1:
                        self.pedirNombres()
                    elif opcionElegida==2:
                        self.desapilar()
                    elif opcionElegida==3:
                        self.imprimirNombres()
                    elif opcionElegida ==4:
                        self.listaInvertida()
                    elif opcionElegida ==5:
                        print("Programa cerrado con éxito :)") 
                        break #Cierro el programa
                else:
                    print("Ingrese una opción entre 1 y 4")"""