vetor = []
contador = 0
for c in range(10):
    vetor.append(int(input("digite um número para a lista ")))
pesquisa = int(input("qual número vc deseja pesquisar? "))
for c in range(10):
    if vetor[c] == pesquisa:
        contador+=1
print(f"o número aparece na lista {contador} vezes")