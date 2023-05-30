# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))

# Função para fazer uma jogada
def fazer_jogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == "-":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

# Função para verificar se o jogo terminou em empate
def empate(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == "-":
                return False
    return True

# Função para verificar se algum jogador venceu o jogo
def vencedor(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Criação do tabuleiro
tabuleiro = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Loop principal do jogo
jogador_atual = "X"

while True:
    imprimir_tabuleiro(tabuleiro)
    linha = int(input("Digite a linha da sua jogada (0-2): "))
    coluna = int(input("Digite a coluna da sua jogada (0-2): "))
    if fazer_jogada(tabuleiro, linha, coluna, jogador_atual):
        if vencedor(tabuleiro, jogador_atual):
            print(jogador_atual, "ganhou o jogo!")
            break
        elif empate(tabuleiro):
            print("O jogo terminou em empate.")
            break
        jogador_atual = "O" if jogador_atual == "X" else "X"
    else:
        print("Essa jogada não é válida. Tente novamente.")
