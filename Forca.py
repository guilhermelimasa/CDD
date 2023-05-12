from random import choice

palavras = ['python', 'java', 'ruby', 'javascript', 'pedro', 'csharp']
palavra = choice(palavras)
letras_ocultas = ['_' for letra in palavra]
tentativas_restantes = 6
letras_corretas = []
letras_erradas = []

while tentativas_restantes > 0:
    print(' '.join(letras_ocultas))
    print(f'Tentativas restantes: {tentativas_restantes}')
    letra = input('Digite uma letra: ')

    if letra in letras_corretas or letra in letras_erradas:
        print('Você já tentou essa letra. Tente outra.')
    elif letra in palavra:
        letras_corretas.append(letra)
        for i, letra_palavra in enumerate(palavra):
            if letra_palavra == letra:
                letras_ocultas[i] = letra
        if '_' not in letras_ocultas:
            print(f'Parabéns! A palavra era {palavra}. Você ganhou!')
            break
    else:
        letras_erradas.append(letra)
        tentativas_restantes -= 1
        print(f'A letra {letra} não está na palavra.')

    print(f'Letras corretas: {letras_corretas}')
    print(f'Letras erradas: {letras_erradas}')

if tentativas_restantes == 0:
    print(f'Infelizmente você perdeu. A palavra era {palavra}.')
