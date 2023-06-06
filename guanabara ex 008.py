while True:
    x = int(input("digite um número: "))
    if x > 0:
        print(f"o sucessor de {x} é {x+1}  e o antecessor é {x-1}")
    else:
        print(f"o sucessor de {x} é {x-1} e o antecessor é {x+1}")
    pergunta = input("vc deseja calcular um novo número? ")
    if pergunta != 'sim':
        break
print("programa encerrado!!!")
