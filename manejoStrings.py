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
    nuevo_set = {}
    for str in cadena:

        if str in nuevo_set:
            nuevo_set[str] = nuevo_set[str]+1
        else:
            nuevo_set[str] = 1

    return nuevo_set


print(contarFrequencias('laluunu'))
