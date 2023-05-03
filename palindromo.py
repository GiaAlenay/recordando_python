def es_palindromo(texto):
    reversa = ''
    for _ in range(len(texto.strip().lower())-1, -1, -1):
        reversa += texto.strip().lower()[_]

    if reversa == texto.strip().lower():
        return True
    return False


print('ab a', es_palindromo('aba'))
