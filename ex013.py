from funcoes import *
while True:
    nome = input("digite o nome do produto: ")
    preco = float(input("digite o preço do produto: "))
    bota(nome, preco)
    pergunta = input("vc deseja inserir mais alguma coisa ? ")
    if pergunta == 'sim':
        continue
    else:
        break
for c in range(len(ab)):
    print(f"o produto {ab[c]}, tem o preço {ba[c]}R$")
