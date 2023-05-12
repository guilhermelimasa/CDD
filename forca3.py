from random import choice

vetor = ['arara', 'coordenada', 'cone', 'guabiraba', 'soneto']
texto = choice(vetor)
lista = ['_'] * len(texto)
tentativas = 6

def win():
    print("parabéns vc venceu")

while tentativas != 0:
    print(' '.join(lista))
    pergunta = input("digite uma letra: ")
    if pergunta in texto:
        for i in range(len(texto)):
            if texto[i] == pergunta:
                lista[i] = pergunta
        if lista == list(texto):
            win()
            break
    else:
        tentativas -= 1
        print(f"Você errou! Você tem {tentativas} tentativas restantes.")
    if tentativas == 0:
        print("Fim de jogo. Você perdeu!")
