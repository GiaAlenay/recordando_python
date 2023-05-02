"""Introducción a python"""

n1 = input('Ingrese el primer numero: ')
n2 = input('Ingrese el segundo número: ')

n1 = int(n1)
n2 = int(n2)

suma = n1+n2
resta = n1-n2
multi = n1*n2
div = n1/n2

resultados = f"""
Resultados de las operaciones entre {n1} y {n2}:
La suma : {suma}
La resta: {resta}
La multiplicación: {multi}
La divición: {div}
"""
print(resultados)
