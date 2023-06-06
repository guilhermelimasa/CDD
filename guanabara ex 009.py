pergunta = 'sim'
while pergunta == 'sim':
    x = int(input("digite um número: "))
    print(f"o dobro de {x} é {x*2} seu triplo é {x*3} e sua raiz quadrada é {x**0.5:.2f}")
    pergunta = input("vc deseja calcular um novo número? ")
print("programa encerrado!")
