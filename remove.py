def frequenzi(word):
    contador = {}
    for i in word:
        if i in contador:
            contador[i] += 1

        else:
            contador[i] = 1
    verificar = 0
    for c in contador:
        if contador[c] > 2:
            return False
        if contador[c] == 2:
            verificar += 1
    if verificar > 1:
        return False
    else:
        return True


print(frequenzi('aazz'))
