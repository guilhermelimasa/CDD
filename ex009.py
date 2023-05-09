texto = 'O rato roeu a roupa do rei de roma'
def L (text):
    cont = 0
    for c in texto:
        if c in "aeiouAEIOU":
            cont += 1
    print(f"o número de vogais é {cont}")
L(texto)
