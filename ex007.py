def funcao(texto):
    cont = 0
    print(texto)
    for c in texto:
        if c != " ":
            cont += 1
    print(f"esse texto tem {cont} palavras")
    for x in reversed(texto):
        print(x, end=" ")


funcao('o rato roeu a roupa do rei de roma')
