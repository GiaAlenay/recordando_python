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


# Dada una lista de cadenas strings, escribe un programa que devuelva una nueva lista
# que contenga solo las cadenas que empiezan por la letra "a".
# Por ejemplo, si strings = ["hola", "adiós", "año", "amor"],
# el resultado debería ser ["adiós", "año", "amor"].

def cadenas_a(lista_cadenas):
    return list(filter(lambda li: li[0].lower() == 'a', lista_cadenas))


print(cadenas_a(["hola", "adiós", "Año", "amor"]))


# Dada una lista de cadenas strings, escribe un programa que devuelva una nueva
# lista que contenga solo las cadenas que sean anagramas de otra cadena en la lista.
# Por ejemplo, si strings = ["cinema", "act", "tar", "cat", "silent"],
# el resultado debería ser ["act", "cat"].

def angramas(lista_cadenas):
    lista_anagramas = []
    for li in lista_cadenas:
        for li2 in lista_cadenas:

            if li != li2 and len(li) == len(li2) and set(li) == set(li2):
                print(li)
                lista_anagramas.append(li)

    return lista_anagramas


print(angramas(["cinema", "act", "tar", "cat", "silent"]))


# Dada una lista de números nums, escribe un programa que devuelva una nueva lista que
# contenga solo las secuencias de números consecutivos más largas de la lista original.
# Por ejemplo, si nums = [1, 2, 3, 5, 6, 7, 8, 9, 10],
# el resultado debería ser [[5, 6, 7, 8, 9, 10]].

def consecutivos(lista_num):
    lista_consecutivos = []
    index = 0
    index2 = 0
    for l1 in range(0, len(lista_num), 1):

        if len(lista_consecutivos) == 0:
            lista_consecutivos.append([lista_num[l1]])
        if lista_consecutivos[index][index2]+1 == lista_num[l1]:
            lista_consecutivos[index].append(lista_num[l1])
            index2 += 1
        else:
            index += 1
            index2 = 0
            lista_consecutivos.append([lista_num[l1]])
    max = []
    for li in lista_consecutivos:

        if len(li) > len(max):
            max = li

    return max


print(consecutivos([1, 2, 3, 5, 6, 7, 8, 9, 10, 14, 15]))


# Dada una lista de cadenas strings, escribe un programa que devuelva una nueva
# lista que contenga solo las subsecuencias comunes más largas entre todas las cadenas
# de la lista. Por ejemplo, si strings = ["abcdefg", "defgabc", "ghijkl"],
# el resultado debería ser ["defg"].

def subsecuencias(lista):
    nueva_lista = [list(li) for li in lista]
    minilista = []
    for sublista in nueva_lista:
        subsecuencia = []
        index = 0
        index2 = 0
        for l1 in range(0, len(sublista), 1):

            if len(subsecuencia) == 0:
                subsecuencia.append([sublista[l1]])
            if ord(subsecuencia[index][index2])+1 == ord(sublista[l1]):
                subsecuencia[index].append(sublista[l1])
                index2 += 1
            else:
                index += 1
                index2 = 0
                subsecuencia.append([sublista[l1]])

        if len(max(subsecuencia, key=len)) > len(minilista):
            minilista = max(subsecuencia, key=len)
    return minilista


print(subsecuencias(["abcdefg", "defgabc", "ghijkl"]))


# Dada una lista de números nums, escribe un programa que devuelva una nueva
# lista que contenga solo los núme eros que sean la suma de dos números distintos
# de la lista original. Por ejemplo, si nums = [2, 3, 4, 6, 8, 9, 10, 12],
# el resultado debería ser [6, 8, 10].
