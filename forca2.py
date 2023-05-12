from random import choice
vetor = ['arara', 'cordenada', 'cone', 'guabiraba', 'soneto']
texto = choice(vetor)
lista = ["_"]*len(texto)
cont = 0
tentativas = 6
def win (numero):
    print("parabéns vc venceu")
for y in range(len(texto)):
    lista.append('_')
    print(lista[y], end=" ")
while tentativas != 0:
    pergunta = input("digite uma letra: ")
    for c in range(len(texto)):
        if texto[c] == pergunta:
            del lista[c]
            lista.insert(c, pergunta)
            print(lista[c], end=" ")

        else:
            print(lista[c], end=" ")
    if lista == list(texto):
        win()
        break
    if pergunta not in texto:
        tentativas -= 1
    if tentativas == 0:
        break

print()
print("fim de jogo")
