# Dado un string s, escribe un programa que invierta la cadena.
# Por ejemplo, si s = "hola", el resultado debe ser "aloh".

def invertir(palabra):
    # re = list(palabra)
    # re.reverse()
    # return ''.join(re)
    return palabra[::-1]


print(invertir('holaaad'))
