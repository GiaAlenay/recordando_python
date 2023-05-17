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


# Escribe una función que tome una lista de palabras como entrada y devuelva 
# un diccionario donde las claves sean las palabras y los valores sean el número
# de veces que aparece cada palabra en la lista.

def lis_to_dic(lista):
    new_dictionary={}
    for li in lista:
        if li in new_dictionary:
            new_dictionary[li]=new_dictionary[li]+1
        else:
            new_dictionary[li]=1
    return new_dictionary
print(lis_to_dic(["lla",'de','ju','lla','na','na','na']))



# Escribe una función que tome dos cadenas de texto como entrada y 
# devuelva True si son anagramas (es decir, si se pueden 
# formar una a partir de las letras de la otra) y False en caso contrario.

def anagramas(str1,str2):
    return sorted(str1)== sorted(str2)

print(anagramas('nana','anna'))



# Validar paréntesis: Escribe una función que tome una cadena de texto que contiene 
# paréntesis y devuelva True si los paréntesis están 
# correctamente balanceados, y False en caso contrario.

def parentesis_balanciado(str):
    counter=0
    for i in str:
        if ord(i)==40:
            counter+=1
        if ord(i)==41:
            counter-=1
    return counter==0
print(parentesis_balanciado("((())))"))

# Encontrar el número faltante: Escribe una función que tome una lista de números 
# del 1 al n (excepto uno) como entrada y devuelva el número faltante.

def faltante(lista):
    order_lista=sorted(lista)
    anterior=order_lista[0]
    for li in range(1,len(order_lista)):
        if anterior+1 !=order_lista[li]:
            return anterior+1
        else:
            anterior=order_lista[li]
    return'estan completos'
print(faltante([1,7,5,6,4,3,2]))


# Calcular el número de inversiones: Escribe una función que tome una lista de números 
# como entrada y devuelva el número de inversiones en la lista. Una inversión se 
# produce cuando un número 
# mayor aparece antes que un número menor en la lista.

def inversiones(lista):
    lista_inversiones=[]
    for i in range(0,len(lista)):
        for a in range(i+1, len(lista)):
            if lista[a]<lista[i]:
                lista_inversiones.append((lista[i],lista[a]))
    return len(lista_inversiones)
print(inversiones([2, 4, 1, 3, 5]))


