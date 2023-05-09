incio = int(input("digite a hora de início do jogo: "))
fim = int(input("digite a hora do fim do jogo: "))
contador = 0
for c in range(incio, fim):
    contador += 1
if contador < 24:
    print(f"o jogo teve {contador} horas.")
else:
    print(f"o jogo bateu as vinte quatro horas, jogo encerrado.")
