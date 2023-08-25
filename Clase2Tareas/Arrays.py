# Tareas clase 2 Arrays
import array as arr
vector = arr.array('i',) #ACTIVIDAD 1
def crearVectorMil2Mil():
    tamaño= 10
    valorinicial = 1000
    for i in range(tamaño+1):
        vector.append(valorinicial)
        valorinicial += 100
    return vector
def imprimirVector(vectoramostrar):
    crearVectorMil2Mil()
    for i in range(len(vectoramostrar)):
        print(f'Numero: {vectoramostrar[i]} Posición: {i}') # FIN ACTIVIDAD 1
imprimirVector(vector)

#Actividad 2
def cargarVectorBucleFor():
    cantnumeros=100
    vectorconfor = arr.array('i',)
    valorinicial=100
    for i in range(cantnumeros+1):
        vectorconfor.append(valorinicial)
        valorinicial+=1
    print(*vectorconfor)

def cargarVectorBucleWhile():
    vectorconwhile=arr.array('i',)
    limite=200
    valorinicial=100
    while valorinicial <= 200:
        vectorconwhile.append(valorinicial)
        valorinicial+=1
    print(*vectorconwhile)
print(f'Vector con for: ',end="")
cargarVectorBucleFor()
print(f'\nVector con while: ',end="")
cargarVectorBucleWhile() #Fin actividad 2

#Actividad 3
def verificarSiEsNumero(numeroAVerificar):
    try:
        int(numeroAVerificar)
        return True
    except Exception as e:
        return False
vector= arr.array('i',[])
def pedirNumeros():
    tamaño=10
    for i in range(tamaño):
         while True:
            numero = input(f"Ingrese su numero{i+1}")
            if verificarSiEsNumero(numero):
                numero = int(numero)
                vector.append(numero)
                break
            else:
                print("Ingrese un numero valido")

def verificarTerminacion():
    pedirNumeros()
    for i in range(len(vector)):
        if vector[i] % 10 in(3,4,8,9):
            print('*',vector[i],end=' ')
        else:
            print(vector[i],end=' ')
verificarTerminacion() #Fin actividad 3

#Actividad 4
from random import *
ganadores= arr.array('i',[]*3)
def sorteo():
    primerdni= 43158258
    ultdni= 44200952
    ganador= randint(primerdni,ultdni)
    cantparticipantes=58
    for i in range(cantparticipantes):
        while True:
            ganador= randint(primerdni,ultdni)
            if ganador not in ganadores:
                ganadores.append(ganador)
                break
    print(f'\n1° Ganador: {ganadores[0]}\n2° Ganador: {ganadores[1]}\n3° Ganador: {ganadores[2]}')
sorteo() #Fin actividad 4





