vetorA = []
vetorM = []
for c in range(10):
    vetorA.append(float(input("digite um número para a lista A: ")))
y = float(input("digite mais um número: "))
for x in range(10):
    vetorM.append(vetorA[x]*y)
    print(vetorM[x])

