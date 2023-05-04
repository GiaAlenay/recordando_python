def frequenzi(word):
    contador = {}
    for i in word:
        if i in contador:
            contador[i] += 1

        else:
            contador[i] = 1

    values = list(contador.values())
    # print(valores)
    min_freq = min(values)
    max_freq = max(values)

    if min_freq == max_freq:
        return True
    elif values.count(min_freq) == 1 and min_freq == 1:
        return True
    elif values.count(max_freq) == 1 and max_freq == min_freq + 1:
        return True
    else:
        return False


print(frequenzi('aassszz'))
