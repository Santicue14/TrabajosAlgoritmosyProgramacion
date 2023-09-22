"""El banco propio de la universidad " BUNPAZ " abre a las 10 AM y otorga 10 turnos desde el 
número 0 al 9 todos los dias. Al banco posee 3 cajas A , B y C para atender estos clientes.
Ud debe realizar un programa que otorgue los números a cada cliente, estos esperan ser
llamados, por las cajas = ['A','B','C'] . Las cajas son asignadas aleatoriamente hasta terminar de atender a todos los clientes.

Haga uso de las funciones aleatorias.

Se le otorgarán los TDA correspondientes de Pila y Cola, estarán en un archivo llamado tda_parcial.py
este debe alojarse en la misma carpeta donde está ejecutando su programa.
recuerde usar from tda_parcial import *

"""
from tda_parcial import *
from random import randint #Importo random para asignar una caja aleatoria

cajas = ["A","B","C"] #Creo un arreglo con las 3 cajas
BUNPAZ  = Cola() #LLamo a la clase como BUNPAZ 
for i in range(0,9+1): #Hago un bucle for para crear los 9 turnos
    BUNPAZ .encolar(i)
    print(f'Turno {i} entregado') #Imprimo el turno ya entregado
print("""
Sistema de atención al cliente
""")
while not BUNPAZ .es_vacia(): #Mientras la cola no esté vacía, imprimo el primer valor y un valor de caja aleatorio entre sus índices
    print(f'Número {BUNPAZ .lista_cola[0]} Caja {cajas[randint(0,2)]}')
    BUNPAZ .desencolar()
#En el archivo de tda_parcial modifiqué la funcion desencolar() y lo dejé así
"""def desencolar(self):
        ''' Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía envia un mensaje de cola vacia. '''
        
        if self.es_vacia():
            print("La cola está vacía")
        else:
            self.lista_cola.pop(0)
           """
