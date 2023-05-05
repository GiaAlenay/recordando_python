# Dada una lista de números nums, escribe un programa que devuelva una nueva lista que
# contenga solo los números pares de la lista original.
# Por ejemplo, si nums = [1, 2, 3, 4, 5, 6], el resultado debería ser [2, 4, 6].

def Lista_Pares(lista):
    # return [li for li in lista if li % 2 == 0]
    return list(filter(lambda li: li % 2 == 0, lista))


print(Lista_Pares([1, 2, 3, 4, 5, 6]))


# Dada una lista de cadenas strings, escribe un programa que devuelva una nueva lista
# que contenga solo las cadenas de longitud mayor o igual a 5.
# Por ejemplo, si strings = ["hola", "python", "mundo", "hoy"],
# el resultado debería ser ["python", "mundo"].

def leng_mayor_5(lista_cadenas):
    # return [li for li in lista_cadenas if len(li) > 4]
    return list(filter(lambda li: len(li) > 4, lista_cadenas))


print(leng_mayor_5(["hola", "python", "mundo", "hoy"]))


# Dada una lista de números nums, escribe un programa que devuelva una nueva
# lista que contenga solo los números que sean múltiplos de 3 o de 5.
# Por ejemplo, si nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
# el resultado debería ser [3, 5, 6, 9, 10].

def multiplos(lista_numeros):
    # return [li for li in lista_numeros if li % 3 == 0 or li % 5 == 0]
    return list(filter(lambda li: li % 5 == 0 or li % 3 == 0, lista_numeros))


print(multiplos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
