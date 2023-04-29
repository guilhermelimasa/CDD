vetor = []
soma = 0
for c in range(4):
    vetor.append(float(input("digite um número: ")))
for x in range(4):
    soma = soma + vetor[x]
media = soma / 4
print(media)