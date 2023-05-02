numero1 = ''
numero2 = ''
operacion = ''


while numero1 != 'salir' or numero2 != 'salir' or operacion != 'salir':

    numero1 = input('Ingrese un numero: ')
    if numero1 == 'salir':
        break
    else:
        numero1 = int(numero1)

    operacion = input("""Escoge la operación a realizar:
        a. Suma
        b. Resta
        c. Multiplicación
        d. División
        """)
    if operacion == 'salir':
        break

    numero2 = input('Ingresa un segundo numero: ')
    if numero2 == 'salir':
        break
    else:
        numero2 = int(numero2)

    if operacion.lower().strip() == 'a':
        print(f"La suma entre {numero1} y {numero2} es : {numero1+numero2}")
    elif operacion.lower().strip() == 'b':
        print(f"La resta entre {numero1} y {numero2} es : {numero1-numero2}")
    elif operacion.lower().strip() == 'c':
        print(
            f"La multiplicación entre {numero1} y {numero2} es : {numero1*numero2}")
    elif operacion.lower().strip() == 'd':
        print(
            f"La división entre {numero1} y {numero2} es : {numero1/numero2}")
