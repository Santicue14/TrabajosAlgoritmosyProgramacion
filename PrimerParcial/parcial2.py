"""Se le otorgarán el TDA correspondientes de Lista ORDENADA, se encuentra  en un archivo para descargar
llamado ListaORDENADA_parcial.py este debe alojarse en la misma carpeta donde está ejecutando 
su programa.
recuerde usar from ListaORDENADA_parcial import *


Combinados = ['CUATRO', 2, 3, 'CINCO', 'SEIS', 4, 'NUEVE', 'DOS', 'CERO', 'TRES', 6, 
'SIETE', 9, 5, 'UNO', 'OCHO', 1, 7, 8]

A. Agregue a una lista ordenada la lista de datos propuesta llamada Combinados, muestre la lista creada.
B. Explique porque se ordenaron los elementos que son las palabras de esa forma.
C. Explique que función cumple el método: metodo_nuevo
D. Realice una operación donde se ponga en práctica el método  metodo_nuevo
E. Cree un método para limpiar(eliminar) la lista creada. Muestre la lista eliminada."""

from ListaORDENADA_parcial import *
ListaAgregar = ['CUATRO', 2, 3, 'CINCO', 'SEIS', 4, 'NUEVE', 'DOS', 'CERO', 'TRES', 6, 'SIETE', 9, 5, 'UNO', 'OCHO', 1, 7, 8]
Combinada = ListaOrdenada()
while ListaAgregar != []: # A)Agregue a una lista ordenada la lista de datos propuesta llamada Combinados, muestre la lista creada.
    Combinada.agregar(str(ListaAgregar.pop(0))) #Convierto cada valor a String, esto lo que logra es que pueda comparar todos los valores entre sí, ya que la lista ordenada utiliza un operador de mayor a menor y, no puede hacer esto entre un String y un Int.
Combinada.ver() 
"""B) Cuando imprimo la lista veo que todos los números normales(que antes eran enteros) están primeros,
esto se debe a que en el orden que los evalúa, siempre están primeros los números y luego las letras,
y luego las letras las evalúa según su orden álfabeticamente, por eso el cinco está antes que el cuatro,
ya que evalúa su primer letra "C", en ambos casos, al repetirse la primer letra, pasa a evaluar la segunda,
y la "I" está antes que la "U"
.
C) El metodo_nuevo lo que hace es mostrar el valor que se encuentra en ese índice, arranca contando desde el 0,
y se corta cuando el contador es igual a la posición buscada, entonces en la posición 0 iría el 1 y así"""
print(f'{Combinada.metodo_nuevo(12)}') #D) Aqui usamos la funcion para mostrar el valor que se encuentra en la posición 12 y muestra el 2
Combinada.limpiar()
"""En el archivo ListaORDENADA_parcial, agregué la función limpiar() que se encarga de desenlazar todos los 
nodos y volver a designar None como la cabeza, luego imprime la lista"""
