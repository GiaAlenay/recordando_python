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

# Escribe una función que tome una lista de números como entrada y devuelva la suma de los números pares.

def sumar_pares_lista(lista):
    return sum([li for li in lista if li%2==0 ])

print(sumar_pares_lista([46,5,8,7,6,1]))

# Escribe una función que tome una lista de números como entrada y devuelva 
# la suma de los números pares.

def largo_cadena(string):
    return len(''.join(string.split()))

print(largo_cadena("welcome to the jungle"))

# Escribe una función que tome una cadena de texto como entrada y devuelva una
#  nueva cadena donde cada letra se desplace un número fijo de posiciones en el 
# alfabeto (por ejemplo, si el número es 2, la letra 'a' se convertirá en 'c', la letra 
# 'b' se convertirá en 'd', y así sucesivamente).

def cadena_desplazada(string,n):
    new_string=[]
    for str in string:
        if ord(str) != 32:
            new_string.append(chr(ord(str)+n))
        else:
            new_string.append(str)

    return ''.join(new_string)
print(cadena_desplazada("Hello World!",1))
