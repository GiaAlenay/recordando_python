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
