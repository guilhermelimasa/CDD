vetorA = []
vetorB = []
soma = []
n = int(input("digite um número: "))
for c in range(n):
    vetorA.append(int(input("digite um número para a lista A: ")))
    vetorB.append(int(input("digite um número para a lista B: ")))
    soma.append(vetorA[c]+vetorB[c])
for x in range(n):
    print(soma[x])
