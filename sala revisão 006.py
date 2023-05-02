somador = 0
while True:
    for c in range(4):
        n1 = float(input("digite a altura: "))
        somador += n1
    media = somador/4
    print(f"a média é {media:.2f}")
    pergunta = input("vc deseja fazer um novo cálculo? ")
    if pergunta == 'não':
        break
print("programa finalizado!!!")
