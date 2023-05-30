confirm = 'sim'
while confirm in 'SIMsimYESyes':
    jogo = [[' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' ']]
    contadorx = 0
    contadoro = 0
    parar = 0
    contador_velha = 0
    condicao = True

    desenho = input('digite X ou O para começar: ').upper()
    while desenho not in ('XO'):
        desenho = input('digite ''exatamente'' X ou O para marcar: ').upper()

    else:
        jogador2 = 'X'
    # printa a tela inicial
    print('jogo da velha!')
    print('============')
    print('Boa sorte!')
    print()
    for x in range(3):
        for y in range(5):
            print(jogo[x][y], end=' ')
        print()
        if x < 2:
            print('=========')
    print()
    while True:

        # cuida de retirar e colocar posição no vetor

        posicaoy = int(input('digite a posição da linha: '))
        while posicaoy < 1 or posicaoy > 3:
            posicaoy = int(input('digite uma posiçãode 1 a 3 para  a linha: '))
        posicaox = int(input('digite a posição da coluna: '))
        while posicaox < 1 or posicaox > 3:
            posicaox = int(input('digite uma posição de 1a 3 para a coluna: '))
        print()
        # cuida de colocar a posição real no vetor
        if posicaox % 2 != 0 and posicaox == 1:
            posicaox -= 1
        elif posicaox % 2 != 0 and posicaox != 1:
            posicaox += 1
        else:
            posicaox = posicaox
        # tratando as regras
        if jogo[posicaoy - 1][posicaox] not in (' '):
            print()
            print('já existe algo marcado aqui!')
            condicao = True
            print()
        else:
            condicao = False
            del jogo[posicaoy - 1][posicaox]
            jogo[posicaoy - 1].insert(posicaox, desenho)
        # ======================
        # print do vetor após alteração em seu local
        for a in range(3):
            for b in range(5):
                print(jogo[a][b], end=' ')
            print()
            if a < 2:
                print('=========')
        # ------------------------------
        # condições para vitória
        # horizontal
        for ch in range(3):
            if jogo[ch][0] == 'X' and jogo[ch][2] == 'X' and jogo[ch][4] == 'X':
                parar = 1
                print("Fim de jogo! X venceu!")
                break
            if jogo[ch][0] == 'O' and jogo[ch][2] == 'O' and jogo[ch][4] == 'O':
                parar = 1
                print("Fim de jogo! O venceu!")
                break

        if parar == 1:
            break
            # cruzado  da esquerda
        if jogo[0][0] == 'X' and jogo[1][2] == 'X' and jogo[2][4] == 'X':
            print("Fim de jogo! X venceu!")
            break
        if jogo[0][0] == 'O' and jogo[1][2] == 'O' and jogo[2][4] == 'O':
            print("Fim de jogo! O venceu!")
            break
        # cc1 = cruzado da direita
        if jogo[2][0] == 'X' and jogo[1][2] == 'X' and jogo[0][4] == 'X':
            print("Fim de jogo! X venceu!")
            break
        if jogo[2][0] == 'O' and jogo[1][2] == 'O' and jogo[0][4] == 'O':
            print("Fim de jogo! O venceu!")
            break

        # cv > contador  vertical
        for cv in range(0, 5, 2):
            if jogo[0][cv] == 'X' and jogo[1][cv] == 'X' and jogo[2][cv] == 'X':
                parar = 1
                print('Fim de jogo! X venceu!')
                break
            if jogo[0][cv] == 'O' and jogo[1][cv] == 'O' and jogo[2][cv] == 'O':
                print('Fim de jogo! O venceu!')
                parar = 1
                break
        if parar == 1:
            break
        # contador_velha > conta se o jogo der velha
        for velha in range(3):
            for cvelha in range(5):
                if jogo[velha][cvelha] == 'X' or jogo[velha][cvelha] == 'O':
                    contador_velha += 1
        if contador_velha == 9:
            print('Deu velha!')
            break
        else:
            contador_velha = 0

        if condicao == True:
            if desenho == 'X':
                desenho = 'X'
            else:
                desenho = 'O'
        else:
            if desenho == 'X':
                desenho = 'O'
            else:
                desenho = 'X'
    confirm = input('Quer Jogar de novo? [S/N]: ')
    if confirm not in ('YESSIMsimSyess'):
        print('Programa encerrado!')
    else:
        continue