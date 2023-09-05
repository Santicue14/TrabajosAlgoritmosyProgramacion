def verificarNumero(numero):
    try:
        numero = int(numero)
        return True
    except Exception:
        print("Ha ingresado un numero inválido, presione enter para continuar")
        return False
resultado= 0
menor = 0
numero_1 = input(f"Ingrese su 1 numero")
numero_2 = input(f"Ingrese su 2 numero")
while True:

        if verificarNumero(numero_1):
            numero_1 = int(numero_1)

            if verificarNumero(numero_2):
                numero_2 = int(numero_2)
                suma = int(numero_1) * int (numero_2)
                if numero_1 == numero_2:
                    print("Los dos números son iguales.")
                elif numero_1 < numero_2:
                    print(f"El numero {numero_1} es menor que {numero_2}")
                    menor = numero_1
                else:
                    print(f"El numero {numero_2} es menor que {numero_1}")
                    menor= numero_2
                resultado = numero_2 * numero_1
                print(f"El resultado entre {numero_1} * {numero_2} = {resultado}")
            for i in range(menor,resultado+1):
                print(i)
            break