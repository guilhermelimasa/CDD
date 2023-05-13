arrai = 'o rato roeu a roupa do rei de roma'
while True:
    letra = input("digite uma letra: ")
    print(f"a letra {letra} aparece {arrai.count(letra)} veze(s)")
    pergunta = input("vc deseja ver uma nova letra?")
    if pergunta != 'sim':
        break
