# Dado un string s, escribe un programa que invierta la cadena.
# Por ejemplo, si s = "hola", el resultado debe ser "aloh".

import re


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
