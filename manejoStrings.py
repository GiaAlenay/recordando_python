import re
# Dado un string s, escribe un programa que invierta la cadena.
# Por ejemplo, si s = "hola", el resultado debe ser "aloh".


def invertir(palabra):
    # re = list(palabra)
    # re.reverse()
    # return ''.join(re)
    return palabra[::-1]


print(invertir('holaaad'))


# Dado un string s, escribe un programa que elimine todos los caracteres que no sean letras del alfabeto inglés.
# Por ejemplo, si s = "Hello! World!", el resultado debe ser "HelloWorld"

def eliminarCaracteres(cadena):
    return ''.join(filter(str.isalpha, cadena))


print(eliminarCaracteres('holi mundo!'))


# Dado un string s, escribe un programa que cuente el número de ocurrencias de cada carácter en la cadena.
# Por ejemplo, si s = "hello", el resultado debe ser {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

def contarFrequencias(cadena):
    contador = {}
    for str in cadena:

        if str in contador:
            contador[str] = contador[str]+1
        else:
            contador[str] = 1

    return contador


print(contarFrequencias('laluunu'))


# Dado un string s, escribe un programa que compruebe si la cadena es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda)
# . Por ejemplo, si s = "racecar", el resultado debería ser True.

def palindromoV2(palabra):
    return palabra == palabra[::-1]


print(palindromoV2('anau'))

# Dado un string s y una subcadena sub, escribe un programa que cuente el número de ocurrencias de la subcadena en la cadena.
# Por ejemplo, si s = "hello world" y sub = "o", el resultado debería ser 2.


def contarSubcadena(cadena, sub):
    # contador = 0
    # for ca in cadena:
    #     if ca == sub:
    #         contador += 1
    # return contador
    return cadena.count(sub)


print(contarSubcadena('holaa', 'a'))

# Dado un string s, escribe un programa que cuente el número de palabras en la cadena.
# Se considera que una palabra es cualquier secuencia de caracteres del alfabeto inglés
# que esté delimitada por espacios en blanco o signos de puntuación.
# Por ejemplo, si s = "Hola, mundo!", el resultado debería ser 2.


def contarPalabras(cadena):
    return len(re.findall(r'\w+', cadena))


print(contarPalabras('hola, como te va !'))


# Dado un string s y una subcadena sub, escribe un programa que reemplace todas las ocurrencias
# de la subcadena en la cadena con otra cadena new_sub.
# Por ejemplo, si s = "hello world", sub = "o" y new_sub = "x",
# el resultado debería ser "hellx wxrld".

def replace(cadena, sub, newsub):
    return cadena.replace(sub, newsub)


print(replace('hola a todos', 'o', 'x'))

# Dado un string s, escribe un programa que devuelva una nueva cadena que contenga solo
# la primera letra de cada palabra en la cadena original.
# Por ejemplo, si s = "Hola, mundo!", el resultado debería ser "H, m!".


def primeraLetra(cadena):
    # la = re.findall(r"\w+", cadena)
    # return [l[0] for l in la]
    # return list(map(lambda l: l[0], la))
    getFirst = 1
    new_list = []
    for str in cadena:
        if (ord(str) > 96 and ord(str) < 123) or (ord(str) > 64 and ord(str) < 91):
            if getFirst == 1:
                new_list.append(str)
                getFirst = 2

        else:
            new_list.append(str)
            getFirst = 1
    return ''.join(new_list)


print(primeraLetra("Hola, mundo!"))


# Dado un string s, escribe un programa que compruebe si todos los caracteres en la cadena
# son únicos (es decir, si no hay caracteres repetidos en la cadena).
# Por ejemplo, si s = "abcdefg",
# el resultado debería ser True, pero si s = "abccdefg", el resultado debería ser False.

def repetidos(cadena):
    # for str in cadena:
    #     if cadena.count(str) > 1:
    #         return False
    # return True

    is_unique = len(cadena) == len(set(cadena))
    return is_unique


print(repetidos('abcdefg'))

# Dado un string s, escribe un programa que devuelva una nueva cadena que contenga
# solo los caracteres que aparecen un número par de veces en la cadena original.
# Por ejemplo, si s = "abbcccddddeeee", el resultado debería ser "bde".


def mostrarPares(cadena):
    diccionario_Cadena = {}
    lista_pares = []
    for str in cadena:
        if str in diccionario_Cadena:
            diccionario_Cadena[str] += 1
        else:
            diccionario_Cadena[str] = 1
    for key in diccionario_Cadena:
        if diccionario_Cadena[key] % 2 == 0:
            lista_pares.append(key)

    return ''.join(lista_pares)


print(mostrarPares('abbcccddddeeee'))
