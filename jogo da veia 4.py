import random


jogarnovamente = 'S'
jogadas = 0
quemjoga = 2
maxjogadas = 9
vitoria = 'n'
veia = [
    [" ", " ", " "], #linha 0 coluna 0/ linha 0 coluna 1/ linha 0 coluna 2
    [" ", " ", " "], #linha 1 coluna 0/ linha 1 coluna 1/ linha 1 coluna 2
    [" ", " ", " "]  #linha 2 coluna 0/ linha 2 coluna 1/ linha 2 coluna 2
]

def tela():
    print("     0     1    2")
    print("0   ", veia[0][0], " | ", veia[0][1] + " | ", veia[0][2])
    print("   -----------------")
    print("1   ", veia[1][0], " | ", veia[1][1] + " | ", veia[1][2])
    print("   -----------------")
    print("2   ", veia[2][0], " | ", veia[2][1] + " | ", veia[2][2])
    print("Jogadas: ", jogadas)

def jogada():
    global quemjoga
    global jogadas
    if quemjoga == 2 and jogadas < maxjogadas:
        try:
            h = int(input("digite a linha que vc quer: "))
            v = int(input(("digite a coluna quer vc quer: ")))
            while veia[h][v] != " ":
                h = int(input("digite a linha que vc quer: "))
                v = int(input(("digite a coluna quer vc quer: ")))
            veia[h][v] = "X"
            quemjoga = 1
            jogadas += 1
        except:
            print("linha e/ou coluna invalida.")

def PCjoga():
    global quemjoga
    global jogadas
    if quemjoga == 1 and jogadas < maxjogadas:
        h = random.randrange(0, 3)
        v = random.randrange(0, 3)
        while veia[h][v] != " ":
            h = random.randrange(0, 3)
            v = random.randrange(0, 3)
        veia[h][v] = "O"
        jogadas += 1
        quemjoga = 2

def vendovitoria():
    global veia
    vitoria = "n"
    simbolo = ["X", "O"]
    for x in simbolo:
        vitoria = "n"
        #verificar linhas
        l = 0
        c = 0
        while l < 3:
            soma = 0
            c = 0
            while c < 3:
                if veia[l][c] == x:
                    soma += 1
                c += 1

            if soma == 3:
                vitoria = x
                break
            l += 1
        if vitoria != "n":
            break
        #verificar colunas
        l = 0
        c = 0
        while c < 3:
            soma = 0
            l = 0
            while l < 3:
                if veia[l][c] == x:
                    soma += 1
                l += 1

            if soma == 3:
                vitoria = x
                break
            c += 1
        if vitoria != "n":
            break
        #verificar primeira diagonal
        soma = 0
        diagonal = 0
        while diagonal < 3:
            if veia[diagonal][diagonal] == x:
                soma += 1
            diagonal += 1
        if soma == 3:
            vitoria = x
            break
        #verificar segunda diagonal
        soma = 0
        diagonal = 0
        diagonac = 2
        while diagonac >= 0:
            if veia[diagonal][diagonac] == x:
                soma += 1
            diagonal += 1
            diagonac -= 1
        if soma == 3:
            vitoria = x
            break
    return vitoria

def redemption():
    jogadas = 0
    quemjoga = 2
    maxjogadas = 9
    vitoria = 'n'
    veia = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]



while jogarnovamente != "N":
    while True:
        tela()
        jogada()
        PCjoga()
        tela()
        vint = vendovitoria()
        if vint != "n" or jogadas > maxjogadas:
            break
    if vint == "X" or vint == "O":
        print(f"fim de jogo, jogador {vint} venceu.")
    else:
        print("DEU VELHA")
    jogarnovamente = input("vc quer jogar novamente? ").upper()
