n = int(input("digite um número qualquer: "))
an = []
bn = []
soma = []
for c in range(n):
    an.append(float(input("digite um número para a lista A: ")))
    bn.append(float(input("digite um número para a lista B: ")))
for y in range(n):
    soma.append(an[y]+bn[y])
for z in range(n):
    print(soma[z])
