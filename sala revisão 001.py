while True:
    x = float(input("digite um número: "))
    while x == 0:
        x = float(input("número inválido, digite outro: "))
    if x < 0:
        print("número negativo ")
    else:
        print("número positivo")
    pergunta = input("vc deseja fazer o cálculo de novo ? ")
    if pergunta == 'não':
        break
print("programa encerrado!!!")
