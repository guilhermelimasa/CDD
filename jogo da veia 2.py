tab = [[' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' ']]
for x in range(3):
    for y in range(5):
        print(tab[x][y], end=' ')
    print()
    if x < 2:
        print('=========')
while True:
    x_ou_bola = input("digite se vc quer X ou O: ")
    vertical = int(input("digite qual linha vc quer: "))
    horizontal = int(input("digite qual coluna vc quer: "))
    if horizontal % 2 != 0 and horizontal == 1:
        horizontal -= 1
    elif horizontal % 2 != 0 and horizontal != 1:
        vertical += 1
    else:
        horizontal = horizontal
    if tab[vertical - 1][horizontal] not in (' '):
        print()
        print('já existe algo marcado aqui!')
        condicao = True
        print()
    else:
        condicao = False
        del tab[vertical - 1][horizontal]
        tab[vertical - 1].insert(horizontal, x_ou_bola)
    del tab[vertical - 1][horizontal]
    tab[vertical - 1].insert(horizontal, x_ou_bola)
    for x in range(len(tab)):
        print(tab[0][x], end=" ")
    print()
    print("========")
    for y in range(len(tab[1])):
        print(tab[1][y], end=" ")
    print()
    print("========")
    for z in range(len(tab[2])):
        print(tab[2][z], end=" ")
