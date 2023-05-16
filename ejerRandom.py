#Escribe una función que calcule el factorial de un número.
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
print(factorial(7))

#Escribe una función que tome una lista como entrada y devuelva una nueva lista con los elementos únicos (sin duplicados).

def listaSinRep(lista):

    return list(set(lista))

print(listaSinRep([1,1,2,3,5,8,2,10,'h']))


# Escribe una función que tome dos números enteros como entrada y 
# devuelva el resultado de la suma de todos los números enteros entre ellos (incluyéndolos).

def suma_entre(n1,n2):
    return sum(range(n1,n2+1))
print(suma_entre(4,8))
