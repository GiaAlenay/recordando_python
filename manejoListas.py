# Dada una lista de números nums, escribe un programa que devuelva una nueva lista que
# contenga solo los números pares de la lista original.
# Por ejemplo, si nums = [1, 2, 3, 4, 5, 6], el resultado debería ser [2, 4, 6].

def Lista_Pares(lista):
    # return [li for li in lista if li % 2 == 0]
    return list(filter(lambda li: li % 2 == 0, lista))


print(Lista_Pares([1, 2, 3, 4, 5, 6]))
