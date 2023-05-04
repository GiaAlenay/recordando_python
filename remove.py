def frequenzi(word):
    contador = {}
    for i in word:
        if contador[i]:
            print('existe')
        else:
            contador[i] = 1
            print('no existe')

    # else:
    #     return True


print(frequenzi('laa'))
