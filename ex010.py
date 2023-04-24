c = 1
escolha = 0
while escolha != 6:
    c = c +1
    n1 = float(input("digite o primeiro número: "))
    n2 = float(input("digite o segundo número: "))
    while True:
        print(""""ESCOLHA UMA OPÇÃO:
        (1)SOMA
        (2)SUBTRAÇÃO
        (3)MULTIPLICAÇÃO
        (4)DIVISÃO
        (5)ESCOLHER NOVOS NÚMEROS
        (6)ENCERRAR PROGRAMA""")

        escolha = float(input("digite um número: "))

        if escolha == 1:
            soma = n1 + n2
            print(f"a soma entre {n1} e {n2} é {soma}")
        elif escolha == 2:
            sub = n1 - n2
            print(f"a divisão entre {n1} e {n2} é {div}")
        elif escolha == 3:
            mult = n1 * n2
            print(f"a multiplicação entre {n1} e {n2} é {mult}")
        elif escolha == 4:
            div = n1 / n2
            print(f"a divisão entre {n1} e {n2} é {div}")
        elif escolha == 5:
            break
        elif escolha == 6:
            print("programa encerrado!!!")
            break